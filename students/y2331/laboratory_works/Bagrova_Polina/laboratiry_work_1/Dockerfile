FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY manage.py /code/
COPY laboratiry_work_1 /code/laboratiry_work_1
COPY db.sqlite3 /code/
COPY autopark /code/autopark

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
