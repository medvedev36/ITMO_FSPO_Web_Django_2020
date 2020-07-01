FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt 
COPY manage.py /code/
COPY Auto_workshop_django /code/Auto_workshop_django
COPY db.sqlite3 /code/
COPY autopark /code/django_app

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]