# End User Guide
Welcome to the ARA User Guide.
# Admin Set Up
For general Set Up please refer to the ARA README.md, this document is for function definitions and documentation and student functionalities.
# Student Usage
Students should select a book from a library curated by their local administrator. They can do this by clicking the book that they wish to select.  
Once students have made their selection they may begin to take notes while perusing the contents of the book which they selected.  
A Student can save their notes at any time and can also hide notes to quiz themselves. They can accomplish this by pressing the 'save' and 'hide/show' button respectively.  
A Student also has the ability to toggle SQ3R note-taking guidance. They can accomplish this by pressing the 'SQ3R' button  
A Student can also delete their notes for a specified book by pressing the 'delete' button  
Finally when a student is done taking notes they can either press the finish button saving their work and bringing them back to the library or they can exit the program which also saves their work.  

Students should note that they can resize the book window as well as the notes window.
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
# GUI funcs
Buttons == Functions + User Input
Buttons:
   Finish -> Save to DB-> go to Book Selection  
   Save -> Save to DB  
   Delete -> Delete from DB after warning  
   Hide -> Hides Notes Window  
   SQ3R -> Toggles SQ3R text  
   Notes (Window) == UI/User Input  
  
Notes (Window):  
   Resizeable Scrollable Text  
   Scrollable line numbers  
   Content(Window) == Read Only, Book Text  

Content (Window):  
   Resizeable Scrollable Text -> Content of Book  
   Book(Object) == Organised Content/Data  
  
Book:  
   Content == Text  
   Author == Text  
   Title == Text  

Notes(Note Object) == Organised User Generated Content/Data  
  
Notes (Note Object):  
   Content == Text  
   Book Title == Text  
   SQ3R =True/False  
