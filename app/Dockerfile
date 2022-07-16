FROM python:3.9-buster

ARG DB_DOCKER_HOST
ARG DB_PORT
ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
#
# ENV POSTGRES_DB=$POSTGRES_DB
# ENV DB_DOCKER_HOST=$BUILD_VERSION
# ENV DB_PORT=$DB_PORT
# ENV POSTGRES_DB=$POSTGRES_DB
# ENV POSTGRES_USER=$POSTGRES_USER
# ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py makemigrations
RUN python manage.py migrate