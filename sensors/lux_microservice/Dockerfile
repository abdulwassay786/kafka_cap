FROM python:3.10-slim-buster
RUN apt-get update && apt-get -y install cron

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab
COPY lux_microservice.py lux_microservice.py


RUN pip install requests

ENV PYTHONPATH /app
##RUN echo $PYTHONPATH

CMD ["cron", "-f"]

