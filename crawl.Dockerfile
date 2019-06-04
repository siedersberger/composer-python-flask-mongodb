FROM python:3.5.2
COPY libdao /var/www/libdao
COPY crawl /var/www/crawl
WORKDIR /var/www/crawl
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt 
ENV MONTH=1
ENV YEAR=2019
ENTRYPOINT python3 consumer_api.py ${MONTH} ${YEAR}