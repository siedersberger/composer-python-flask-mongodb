# My crawilling with python (mycrawling-py)

## Description
This project use the stackoverflow API for get informations about the questions made on a specific period of time.

The project is divided by the follow modules:
- Data base: MongoDB;
- Crawl: responsable for collect the information from stackoverflow API through stackAPI wrapper and store on the Mongo data base;
- App: responsable for the interface with the user (the app runs in 127.0.0.1:5000)

## Main commands
- docker-compose build 
- docker-compose up -d
- docker-compose down
