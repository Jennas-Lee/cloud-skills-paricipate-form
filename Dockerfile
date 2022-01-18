FROM public.ecr.aws/docker/library/python:3.10.1

WORKDIR /app

ADD . /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install uwsgi
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["uwsgi", "-i", "/app/uwsgi/uwsgi.ini"]
