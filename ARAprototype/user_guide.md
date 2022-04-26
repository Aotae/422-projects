# End User Guide
Welcome to the ARA User Guide.
# Admin Set Up
For general Set Up please refer to the ARA README.md, this document is for function definitions and documentation.
# MDBClient funcs  
Insert_Notes:POST
->(notes) ->void
takes in the notes that need to be inserted into the Note Collection  

Insert_Books:POST  
->(book) ->void  
takes in the book that needs to be inserted into the Book Collection

Update_Notes:PUT  
->(id,notes) ->void  
takes in the id of a note and  Overwrite the notes at id with object 'notes'  

Delete_Notes:DELETE  
->(id) ->void  
takes in the id of a note and removes it from the Notes Collection  

Delete_Books:DELETE  
->(id) ->void  
takes in the id of a book and removes it from the Book Collection  

Delete_Library:DELETE  
->() ->void  
takes in no args and drops the Book Collection (Library)  

Get_Notes:GET  
->(id) -> Document = dict{}  
Retrieves the notes at specified id from Note Collection  

Get_Books:GET  
->(id) ->Document = dict{}  
Retrieves the Book at specified id from Book Collection  

Get_Library:GET  
->() ->array[] of Document = dict{}  
takes in no args and returns all documents in Book Collection as an array  
   
Helper Functions:  
  
connect: connects to mdb server  
Used by all, URI= localhost:27017 for non deployment purposes  
  
note_exists: check if notes exist for a certain book  
Used by Update_Notes  

Delete_note-library:DELETE  
#DO NOT USE ONLY USED IN TESTING  
