# My crawilling with python and mongodb (mycrawling-py)

## Description
This project use the stackoverflow API for get informations about the questions made on a specific period of time.

The project is composed by the follow modules:
- **Data base**: MongoDB;
- **Crawl**: responsible for collect and store data from stackoverflow API;
- **App**: responsible for the interface with the user (the app runs in * *127.0.0.1:5000* *).

## App start
Each module runs into a docker container, wich is necessary for run the app. To start the application, you have to execute the follow steps:
1. Clone or download this repository
2. Into the directory, execute these commands:
    1. docker-compose build 
    2. docker-compose up -d
    3. docker-compose down

### Operation
While the App module show informations stored in data base , the Crawl module stores data in data base independently. When you run the project from docker commands cited above, the Crawl module runs with default inputs (MONTH and YEAR) for store initial data in the data base. If you want to add more data to the data base, specifying anothers inputs, you can execute the follow command:
- docker exec mycrawl python3 consumer_api.py MONTH YEAR
