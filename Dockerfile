FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code-backend
COPY requirements.txt /code-backend/
RUN pip install -r requirements.txt
COPY blog /code-backend/