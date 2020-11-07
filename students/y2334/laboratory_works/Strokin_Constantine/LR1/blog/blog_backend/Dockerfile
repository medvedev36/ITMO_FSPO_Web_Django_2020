FROM python:3
ENV PYTHONUNBUFFERED 1


WORKDIR /code
COPY requirements.txt /code/
COPY db.sqlite3 /code/
COPY db.sqlite3 /code/
ADD db.sqlite3 /code/
ADD db.sqlite3 /code/
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python","manage.py","runserver"]