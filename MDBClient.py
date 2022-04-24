import pymongo
import GUI
from pymongo import MongoClient

#connects to the mongodb database and checks to see if its valid.
def connect():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    return client
def insert_notes(notes):
    # inserts one document into the library collection
    # a document includes A users, Notes and the Book text of which the user is taking notes for
    client = connect()
    print("Hey we got here")
    db = client["ARA_books"]
    collection = db["note-library"]
    collection.insert_one(notes)
    
def insert_books(book):
    client = connect()
    db = client["ARA_books"]
    collection = db["library"]
    collection.insert_one(book)
def update(id):
    pass

def delete(id):
    pass

def get_notes(id):
    client = connect()
    db = client["ARA_books"]
    collection = db["note-library"]
    return collection.find_one(id)
def get_books(id):
    pass
def getlibrary():
    pass

