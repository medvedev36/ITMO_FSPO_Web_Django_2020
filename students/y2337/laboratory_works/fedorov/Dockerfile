FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY ./manage.py ./
COPY ./carsharing ./carsharing
COPY ./backend ./backend

RUN python ./manage.py migrate