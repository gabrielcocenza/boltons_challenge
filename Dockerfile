FROM python:3.7.5-buster
MAINTAINER Gabriel Cocenza <gabrielcocenza@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

COPY . .
RUN pip install -r requirements.txt


