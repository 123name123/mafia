import os

import grpc
import proto.struct_pb2 as pb2
import proto.struct_pb2_grpc as pb2_grpc

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

channel = grpc.insecure_channel("0.0.0.0:8080")
stub = pb2_grpc.MyMafiaEventsStub(channel)


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
    print(user)
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
            avatar.save(f'uploads/avatar{username}.jpg')
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
