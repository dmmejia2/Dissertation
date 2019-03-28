from pymongo import MongoClient

class MongoConnect(object):
    @staticmethod
    def get_connection():
        return MongoClient("mongodb://@localhost:27017/")