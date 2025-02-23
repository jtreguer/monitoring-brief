FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

COPY gunicorn_start.sh .

RUN chmod +x ./gunicorn_start.sh

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
# CMD ["./gunicorn_start.sh"]