FROM python

WORKDIR /worker
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y wkhtmltopdf
ENTRYPOINT [ "python", "worker.py" ]