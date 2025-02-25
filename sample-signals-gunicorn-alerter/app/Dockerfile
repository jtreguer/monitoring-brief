FROM python:3.11-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD app.py /var/server/app/app.py

ADD wsgi.py /var/server/wsgi.py

WORKDIR /var/server/

EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000 -w 4 wsgi:app
