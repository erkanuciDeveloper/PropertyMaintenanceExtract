import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pymongo import MongoClient
from config import Config

class MongoDBClient:
    def __init__(self):
        try:
            self.client = MongoClient(Config.DB_HOST, Config.DB_PORT)
            self.db = self.client[Config.DB_NAME]
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    def insert_many(self, collection_name, data):
        try:
            collection = self.db[collection_name]
            collection.insert_many(data)
        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")
            raise

    def close(self):
        self.client.close()

