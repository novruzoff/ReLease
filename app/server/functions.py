# Common functions for the server to perform CRUD operations on the database
# Connect to the database

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI = "mongodb+srv://emiliakrichevsky:<>@release0.dg5ey5q.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server

def connect():
    client = MongoClient(URI, server_api=ServerApi('1'))   
# Connect to the database    
    db = client["ReLease"]
# Get a collection from the database
    collection = db["SampleData"]
    return collection

# Get all documents from a collection
def get_all_documents():
    collection = connect()
    cursor = collection.find({})
    return cursor
# for document in cursor:
#     print(document)
# Count the number of documents in a collection

# Get a single document from a collection

# Query for a single document from a collection