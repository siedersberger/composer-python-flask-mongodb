# My crawilling with python and mongodb (mycrawling-py)

## Description
This project use the stackoverflow API for get informations about the questions made on a specific period of time.

The project is composed by the follow modules:
- **Data base**: MongoDB;
- **Crawl**: responsable for collect the information from stackoverflow API through stackAPI wrapper and store on the Mongo data base;
- **App**: responsable for the interface with the user (the app runs in * *127.0.0.1:5000* *)

## App start
Each module runs into a docker container, wich is necessary for run the app. To start the application, you have to execute the follow steps:
1. Clone or download this repository
2. Into the directory, execute these commands:
    1. docker-compose build 
    2. docker-compose up -d
    3. docker-compose down
