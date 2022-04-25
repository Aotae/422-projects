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
