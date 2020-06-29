FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY manage.py /code/
COPY laboratory_work_1 /code/laboratory_work_1
COPY db.sqlite3 /code/
COPY kugachFinal /code/kugachFinal

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]