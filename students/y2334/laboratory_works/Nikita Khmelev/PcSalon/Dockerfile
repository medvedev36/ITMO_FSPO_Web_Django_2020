FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY manage.py /code/
COPY PcSalon /code/PcSalon
COPY db.sqlite3 /code/
COPY Base /code/Base
COPY templates /code/templates

#CMD {"python3", "manage.py", "runserver", "0.0.0.0:80"}
