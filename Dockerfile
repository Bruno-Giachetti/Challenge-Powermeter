FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY . ./app
WORKDIR /app/ejercicio_1/
RUN pip install -r requirements.txt
