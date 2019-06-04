FROM python:3.5.2
MAINTAINER Siedersberger
COPY libdao /var/www/libdao
COPY app /var/www/app
WORKDIR /var/www/app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt 
ENTRYPOINT python3 main.py
EXPOSE 5000