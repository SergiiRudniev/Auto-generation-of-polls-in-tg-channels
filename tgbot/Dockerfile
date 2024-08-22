FROM python:3.12

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir aiogram g4f curl_cffi python-dotenv

CMD ["python", "main.py"]
