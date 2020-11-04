FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY ./manage.py ./
COPY ./fur_shop ./fur_shop
COPY ./Rusilova_django ./Rusilova_django
COPY ./Templates ./templates

RUN python manage.py makemigrations
RUN python manage.py migrate
