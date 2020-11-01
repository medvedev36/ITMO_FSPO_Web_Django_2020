FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY ./manage.py ./
COPY ./furs ./furs
COPY ./app ./app
COPY ./templates ./templates

RUN python manage.py makemigrations
RUN python manage.py migrate
