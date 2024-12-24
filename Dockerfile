FROM python:3.11

RUN pip install flask gunicorn

COPY entrypoint.py /app/entrypoint.py

WORKDIR /app

CMD exec gunicorn entrypoint:app
