FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /laborotiry_work_1/
COPY req.txt /laborotiry_work_1/
COPY db.sqlite3 /laborotiry_work_1/
COPY manage.py /laborotiry_work_1/
RUN pip install -r req.txt
COPY . /laborotiry_work_1/
