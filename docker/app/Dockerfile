FROM python


WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y wkhtmltopdf
EXPOSE 3001
ENTRYPOINT [ "python", "rest_api.py" ]