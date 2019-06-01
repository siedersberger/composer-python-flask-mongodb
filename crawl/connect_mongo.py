from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.dbstack
questions_collection = db.questions_collection



