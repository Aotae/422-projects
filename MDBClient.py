import pymongo
import GUI
from pymongo import MongoClient

#connects to the mongodb database and checks to see if its valid.
def connect():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    return client
def insert_notes(notes):
    # inserts one document into the 'note-library' collection
    # a document includes a User's notes for a specified book
    client = connect()
    print("Hey we got here")
    db = client["ARA_books"]
    collection = db["note-library"]
    collection.insert_one(notes)
    
def insert_books(book):
    # inserts one document into the 'library' collection
    # a document includes information on a book such as title and author as well as a cover image
    client = connect()
    db = client["ARA_books"]
    collection = db["library"]
    collection.insert_one(book)
def update(id):
    # Put request that will update a users notes on a specified book by id
    pass

def delete(id):
    # delete request that will delete a users notes on a specified book by id
    pass

def get_notes(id):
    # gets the notes from the 'note-library' collection according to bookname(id)
    client = connect()
    db = client["ARA_books"]
    collection = db["note-library"]
    return collection.find_one(id)
def get_books(id):
     # gets a book from the 'library' collection according to bookname(id)
    client = connect()
    db = client["ARA_books"]
    collection = db["library"]
    return collection.find_one(id)
    
def getlibrary():
     # returns all of the resources in the 'library' collection
    pass

