FROM python:3.12

WORKDIR /app

RUN apk add --no-cache postgresql-dev

COPY . /app

RUN pip install -r requirements.txt

ENV ENV_PATH .env.development

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
