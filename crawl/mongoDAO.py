from pymongo import MongoClient

class ConnectionDAO:

    def __init__(self, hostname, portnumber=27017):
        self.__client = MongoClient(host=hostname, port=portnumber)
        self.__db = self.client.dbstack
        self.__questions_collection = self.db.questions_collection

    @property
    def client(self):
        return self.__client

    @property
    def db(self):
        return self.__db

    @property
    def questions_collection(self):
        return self.__questions_collection

class QuestionDAO:

    def __init__(self, questions_collection):
        self.questions_collection = questions_collection
        

    def add_question(self, question):
        question["_id"] = question["question_id"]
        key = {"_id":question["question_id"]}
        insert = {"$set":question}
        self.questions_collection.update_one(key, insert, upsert=True)


