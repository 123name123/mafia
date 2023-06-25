FROM python

WORKDIR /server
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 10000
ENTRYPOINT [ "python", "server.py" ]