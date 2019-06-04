from pymongo import MongoClient

class ConnectionDAO:

    def __init__(self, hostname="localhost", portnumber=27017):
        self.__client = MongoClient(host=hostname, port=portnumber)
        self.__db = self.client.dbstack

    @property
    def client(self):
        return self.__client

    @property
    def db(self):
        return self.__db

class QuestionDAO:

    def __init__(self, db):
        self.questions_collection = db["questions_collection"]
        
    def find_tag(self, selected_tag):
        return self.questions_collection.find({"tags":selected_tag},{"tags": 1, "_id": 0})

    def add_question(self, question):
        ''' Defines a _id for the question and verify if this id is unique. 
            After that, if the question not exists yet, it will save in data base.
        '''
        question["_id"] = question["question_id"]
        key = {"_id":question["question_id"]}
        insert = {"$set":question}
        self.questions_collection.update_one(key, insert, upsert=True)


