FROM ubuntu:latest
# FROM python:3.7

RUN apt-get update && apt-get -y install cron vim python3-pip

WORKDIR /app

RUN pip install ovh requests python-dotenv

COPY ovh-dns-refresh-crontab /etc/cron.d/ovh-dns-refresh-crontab
COPY main.py /app/main.py
COPY .env /app/.env

RUN chmod 0644 /etc/cron.d/ovh-dns-refresh-crontab
RUN /usr/bin/crontab /etc/cron.d/ovh-dns-refresh-crontab

# run crond as main process of container
CMD ["cron", "-f"]
