import pymongo
import GUI
from pymongo import MongoClient

#connects to the mongodb database and checks to see if its valid.
client = pymongo.MongoClient("mongodb+srv://Aotae:<Aotae>@422notebook.j0r5l.mongodb.net/ARA_books?retryWrites=true&w=majority")
db = client.test


