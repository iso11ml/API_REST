from pymongo import MongoClient

class MongoDBConnection:
    __instance = None
    
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if MongoDBConnection.__instance == None:
            MongoDBConnection()
        return MongoDBConnection.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MongoDBConnection.__instance != None:
            raise Exception("Esta clase es singleton!")
        else:
            MongoDBConnection.__instance = self
            self.client = MongoClient('localhost', 27017)
            self.db = self.client['test']
    
    def get_database(self):
        return self.db