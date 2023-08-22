FROM python:3.11.2-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Use the environment variables directly in the Dockerfile
ENV REDIS_HOST $REDIS_HOST
ENV REDIS_PORT $REDIS_PORT
ENV DB $DB
ENV CORS_ALLOWED_ORIGINS $CORS_ALLOWED_ORIGINS

COPY . /app/

EXPOSE 8000