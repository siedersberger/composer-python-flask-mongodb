from pymongo import MongoClient

class ConfigManager:
    __instance = None
    
    @staticmethod
    def instance():
        if not ConfigManager.__instance:
            ConfigManager.__instance = {
                "mongo_port": 27017,
                "mongo_host": "mongodb"
            }
        return ConfigManager.__instance

class ConnectionDAO:
    __instance = None
    
    @staticmethod
    def instance():
        if not ConnectionDAO.__instance:
            configs = ConfigManager.instance()
            ConnectionDAO.__instance = MongoClient(
                port=configs["mongo_port"],
                host=configs["mongo_host"]
            )
        return ConnectionDAO.__instance

# class ConnectionDAO:

#     def __init__(self, hostname="localhost", portnumber=27017):
#         self.__client = MongoClient(host=hostname, port=portnumber)
#         self.__db = self.client.dbstack

#     @property
#     def client(self):
#         return self.__client

#     @property
#     def db(self):
#         return self.__db

class QuestionDAO:

    def __init__(self):
        self.__db_client = ConnectionDAO.instance()
        self.__questions_collection = self.__db_client.dbstack["questions_collection"]
        
    def find_tag(self, selected_tag):
        return self.__questions_collection.find({"tags":selected_tag},{"tags": 1, "_id": 0})

    def find_all_documents(self):
        return self.__questions_collection.find()

    def add_question(self, question):
        ''' Defines a _id for the question and verify if this id is unique. 
            After that, if the question not exists yet, it will save in data base.
        '''
        question["_id"] = question["question_id"]
        key = {"_id":question["question_id"]}
        insert = {"$set":question}
        self.__questions_collection.update_one(key, insert, upsert=True)
