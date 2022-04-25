# DOCUMENTATION  
## ARA Architecture
![alt text](https://github.com/Aotae/422-projects/blob/main/ARAprototype/Documentation/ARAArchitecture.PNG)  
Our Software can be decomposed into 3 major components the GUI, The B/N(BOOK/NOTE) SERVER and the B/N(BOOK/NOTE) Database. It can be further decomposed to find 2 minor subcomponents of the B/N Database The Book Collection and Note Collection. On a slightly higher layer of abstraction our software follows a Client-Server Model.  
  
# Major Components  
## GUI
The Graphical User Interface (GUI) is the client where A User can select a book from a library maintained by an Administrator. Once a book is Selected The User will be met with a note-taking screen made up of three windows. The first window (Content Window) contains the content of the book in a scrollable text object. The second window (UI Window) contains UI for saving a User's Notes, Deleting a User's Notes, Finish note-taking and go back to library, Toggle SQ3R Guidance, and Hide Notes. The third window (Note Window) is combined with the second window and contains as Scrollable text object which the user can edit and a line counter on the side. The Note window is resizable as is the content window.  
## B/N SERVER
The B/N Server is how the GUI communicates with the rest of the system. All data must pass through the B/N Server before an event can happen.  
The B/N Server holds functions to insert,delete,update and get both books and notes. It achieves this by communicating with the B/N Database which then communicates with its sub components to fetch the data that the Server and in turn the Client/GUI requested. Some of the functions in the B/N Server are only accesible to administrators but for the purpose of testing currently all of the B/N Server functions are avialable to any user for now though the GUI has no way of calling them. 
## B/N DATABASE
The B/N DATABASE is where both Books and Notes are stored. Notes are stored in a 'note-library' collection that is created on the first insertion of a document and books are stored in a seperate collection 'library' which is also created upon the first insertion of a document. The Database is a non-relational database as Users will be inserting/updating values on a regular basis which lead us to believe that a Mongodb or non-SQL database would be more advantageous performance wise. This is due to the fact that a Query wouldn't have to look through multiple tables to fetch a response though considering how we only have what would essentially only be two tables this performance boost seems negligible. The other reason we decided to continue with a MongoDB/Non relational Database is that one of our group members had experience with MongoDB while no one else had a prefrence.

# Minor Components

## Note Collection && Book Collection
The note collection functioned as our 'note-library' and was the actual object which held our 'note' documents while the B/N Database holds collections. We believe that this distinction should be made in our architecture because in a MongoDB database most functions to insert/delete are functions directly called by a collection object rather than the database. In essence the collection acts as a table in a relational database. We also must make a distinction between that which is stored in this collection, that being 'note' objects, and other collections. This is because if we simply stored both notes and books in the same collection finding/getting documents would be much harder as ids piled up. So we make this distinction between collections and databases along with what collections are responsible for what.

# Client-Server Model
Our Software essentially follows a Client-Server model as it has a Client (GUI) which communicates with a server (B/N Server) which then serves data back to the client after it has fetched it from somewhere. The only major difference in our architecture is that we don't encapsulate the Database and its componenets into just a 'Server' Component. This is because we find value in having a slightly less abstract model closer to a representation than a model.


