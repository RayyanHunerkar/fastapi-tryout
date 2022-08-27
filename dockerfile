# syntax = docker/dockerfile

FROM python:3.10-alpine3.13
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /fastapi
COPY requirements.txt /fastapi/
RUN apk update
RUN apk add gcc python3-dev musl-dev libffi-dev
RUN pip install -r requirements.txt
COPY . /fastapi/