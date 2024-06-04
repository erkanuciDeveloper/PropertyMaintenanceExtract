import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class Config:
    DB_HOST = 'localhost'
    DB_PORT = 27017
    DB_NAME = 'salesdb'
