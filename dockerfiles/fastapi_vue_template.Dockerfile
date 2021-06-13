FROM python:3.6.9
MAINTAINER Ilya Soltanov <piccadillable@gmail.com>
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /fastapi_vue_template/requirements.txt
WORKDIR /fastapi_vue_template
RUN pip install -r requirements.txt
COPY . /fastapi_vue_template
