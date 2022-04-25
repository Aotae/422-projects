import fileinput
import MDBClient
from MDBClient import insert_books, delete_books, delete_library, get_books, get_library
"""
Use this script to populate the database with sample data
"""
def insert_library():
    MDBClient.insert_books({"name":"DUNE","content":"This is the book Dune,\nWe don't have the license to it\nso have some filler text\n","author":"Frank Herbert"})
    MDBClient.insert_books({"name":"DUNE_Messiah","content":"This is the book Dune,\nWe don't have the license to it\nso have some filler text\n","author":"Frank Herbert"})
    MDBClient.insert_books({"name":"DUNE_God_Emperor","content":"This is the book Dune,\nWe don't have the license to it\nso have some filler text\n","author":"Frank Herbert"})
    MDBClient.insert_books({"name":"DUNE_Children_of_Dune","content":"This is the book Dune,\nWe don't have the license to it\nso have some filler text\n","author":"Frank Herbert"})

def main():
    insert_library()

main()