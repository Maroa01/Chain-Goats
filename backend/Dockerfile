FROM python:3.9-slim-buster

#setting work directory

RUN mkdir /backend
WORKDIR  /backend

#env variables
ENV PYTHONNUNBUFFERED 1
ENV PYTONDONTWEITEBYTECODE 1

# install psycopg dependencies
 RUN apt-get update && apt-get install -y \
     build-essential \
     libpq-dev \
     && rm -rf /var/lib/apt/lists/*


#install dependencies
RUN pip install --upgrade pip
RUN pip install -U setuptools
COPY requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
COPY app/ /backend/app
