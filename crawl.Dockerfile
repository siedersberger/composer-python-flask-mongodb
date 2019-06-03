FROM python:3.5.2
MAINTAINER Siedersberger
COPY crawl /var/www/crawl
WORKDIR /var/www/crawl
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt 
ENTRYPOINT python3 consumer_api.py