from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client.dbstack
questions_collection = db.questions_collection



