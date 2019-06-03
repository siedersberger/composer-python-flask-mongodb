from pymongo import MongoClient

class Mongo_connection:

    def __init__(self, hostname, portnumber=27017):
        self.client = MongoClient(host=hostname, port=portnumber)
        self.db = self.client.dbstack
        self.questions_collection = self.db.questions_collection

# client = MongoClient('localhost', 27027)
# db = client.dbstack
# questions_collection = db.questions_collection