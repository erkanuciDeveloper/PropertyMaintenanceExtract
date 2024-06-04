from pymongo import MongoClient
from config import Config

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(Config.DB_HOST, Config.DB_PORT)
        self.db = self.client[Config.DB_NAME]

    def insert_many(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_many(data)

    def close(self):
        self.client.close()
