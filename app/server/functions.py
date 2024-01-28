"""
Contains common functions for the server to perform CRUD operations on the MongoDB database.

It includes functions to connect to the database, retrieve all documents from a collection, 
and potentially more functions that are not shown in the provided excerpt.

The database connection is established using the pymongo library. The URI for the MongoDB server 
and the server API version are defined at the top of the module.

Functions:
    connect(): Connects to the database and returns a collection object.
    get_all_documents(): Retrieves all documents from the collection and returns a cursor object.
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

URI = "mongodb+srv://user1:mchacks123@release0.dg5ey5q.mongodb.net/?retryWrites=true&w=majority"


def connect():
    """
    Connects to the database and returns a collection object.

    Returns:
        pymongo.collection.Collection: The collection object representing the collection.
    """
    client = MongoClient(URI, server_api=ServerApi("1"), tlsAllowInvalidCertificates=True)
    # Connect to the database
    db = client["ReLease"]
    # Get a collection from the database
    collection = db["SampleData"]
    return collection

def get_all_documents():
    """
    Get all documents from the collection.

    Returns:
        pymongo.cursor.Cursor: A cursor object representing the result of the query.
    """
    collection = connect()
    cursor = collection.find({})
    return cursor

# Count the number of documents in a collection

# Get a single document from a collection

# Query for a single document from a collection
