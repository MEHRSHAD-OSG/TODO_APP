FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip -i https://mirror-pypi.runflare.com/simple
RUN pip3 install -r requirements.txt -i https://mirror-pypi.runflare.com/simple


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
