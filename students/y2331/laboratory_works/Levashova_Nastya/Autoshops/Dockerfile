FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPRY req.txt /code/
RUN pip install -r req.txt

COPY manage.py /code/
COPY Autoshops /code/Autoshops
COPY autoApp /code/autoApp

#CMD {"python3", "manage.py", "runserver", "0.0.0.0:8000"}
