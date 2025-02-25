FROM python:3.9-slim

WORKDIR /server/app

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /server

COPY . .

EXPOSE 5000

# COPY gunicorn_start.sh .

# RUN chmod +x ./gunicorn_start.sh

CMD ["gunicorn", "wsgi:app", "-c", "gunicorn.conf.py"]
# CMD ["./gunicorn_start.sh"]