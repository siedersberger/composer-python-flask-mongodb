FROM python:3.5.2
MAINTAINER Siedersberger
COPY app /var/www/app
WORKDIR /var/www/app
RUN pip install --upgrade pip
RUN pip3 install pymongo==3.8.0
RUN pip3 install Flask==1.0.3
ENTRYPOINT python3 main.py
EXPOSE 5000