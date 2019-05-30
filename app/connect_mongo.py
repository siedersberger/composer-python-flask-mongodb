from pymongo import MongoClient

client = MongoClient("mongodb", 27017)
db = client.test
alunos_collection = db.alunos


