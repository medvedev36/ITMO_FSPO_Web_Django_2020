FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/final_lab
WORKDIR /usr/src/final_lab
RUN mkdir -p /var/log/platform_admin
COPY . /usr/src/final_lab
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"] 