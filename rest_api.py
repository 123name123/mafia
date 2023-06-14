import os

import grpc
import proto.struct_pb2 as pb2
import proto.struct_pb2_grpc as pb2_grpc

from flask import Flask, render_template, request, redirect, jsonify
from flask_restful import Resource, Api
from rq import Queue
from rq.job import Job
from redis import Redis
from rq.registry import StartedJobRegistry
import pdfkit
from stats import generate_statistics
from worker import conn

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = 'uploads'
api = Api(app)
redis_conn = Redis()
queue = Queue(connection=redis_conn)

channel = grpc.insecure_channel("0.0.0.0:2000")
stub = pb2_grpc.MyMafiaEventsStub(channel)

q = Queue(connection=conn)


@app.route('/stats', methods=['POST'])
def process_stats_request():
    player_name = request.json['player_name']
    job = q.enqueue(generate_statistics, player_name)
    return jsonify({'job_id': job.id}), 202


@app.route('/stats/<job_id>', methods=['GET'])
def get_stats_result(job_id):
    job = Job.fetch(job_id, connection=conn)
    if job.is_finished:
        result = job.result
        return jsonify(result), 200
    elif job.is_failed:
        return jsonify({'error': 'Failed to generate statistics.'}), 500
    else:
        return jsonify({'status': 'in progress'}), 202


@app.route("/")
def get_all_users():
    response = stub.GetUsersInfo(
        pb2.GetUsersInfoRequest()
    )
    print(response.user_list)
    result = [name for _, name in response.user_list.items()]
    return render_template('index.html', users=result)


@app.route('/user/<username>')
def user_profile(username):
    response = stub.GetUserInfo(
        pb2.GetUserInfoRequest(username=username)
    )
    if not response.status:
        return "No such user!"
    user = response.user_info
    user["username"] = username
    user['path'] = "../static/" + user["path"]
    if not user:
        return 'Пользователь не найден'
    return render_template('profile.html', user=user)


@app.route('/user/<username>/edit', methods=['GET', 'POST'])
def edit_user(username):
    response = stub.GetUserInfo(
        pb2.GetUserInfoRequest(username=username)
    )
    if not response.status:
        return "No such user!"
    user = response.user_info
    user["username"] = username

    if request.method == 'POST':
        user['username'] = request.form['username']
        user['email'] = request.form['email']
        user['gender'] = request.form['gender']

        # Обработка загрузки нового аватара
        if 'avatar' in request.files:
            avatar = request.files['avatar']
            avatar.save(f'static/avatar{username}.jpg')
            user['avatar'] = f'avatar{username}.jpg'

        response = stub.EditUser(
            pb2.EditUserRequest(username=username,
                                image_path=user["avatar"],
                                email=user["email"],
                                gender=user["gender"])
        )

        return redirect(f'/user/{username}')

    return render_template('edit.html', user=user)


if __name__ == "__main__":
    app.run()
