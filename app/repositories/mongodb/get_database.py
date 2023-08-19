import os
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
    client = MongoClient(CONNECTION_STRING)
    return client["educai"]
