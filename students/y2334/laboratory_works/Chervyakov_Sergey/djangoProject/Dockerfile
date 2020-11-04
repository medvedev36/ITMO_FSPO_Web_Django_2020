FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY manage.py /code/
COPY djangoProject /code/djangoProject
COPY db.sqlite3 /code/
COPY pla /code/pla
COPY templates /code/templates

#CMD {"python3", "manage.py", "runserver", "0.0.0.0:80"}
