FROM python:3.7
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/code
WORKDIR /code/SAPApp

RUN mkdir -p /home/code
RUN mkdir -p /code/SAPApp

# Install packages
COPY requirements.txt /code
RUN pip install pip -U
RUN pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple
RUN pip install -r /code/requirements.txt

# Install pgsql client
RUN apt-get update && apt-get install -y \
    postgresql-client

CMD []