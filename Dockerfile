FROM python:3.7

RUN apt-get update && apt-get -y install cron vim

WORKDIR /app

RUN pip install ovh requests python-dotenv

COPY crontab /etc/cron.d/crontab
COPY main.py /app/main.py
COPY .env /app/.env

RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container
CMD ["cron", "-f"]