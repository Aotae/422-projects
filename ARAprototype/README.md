# ARA (Active Reading Assistant)

ARA is a program which helps a reader take active notes using SQ3R (Survey, Question, Read, Recite, Review)
This is not a production level product and therefore URIs used to connect are all local rather than real URIs.  
It would be trivial to get the Server running using Mongo Atlas to run as a cloud service but the SRS for the project asked us to  
not use cloud services.

## Installation
## MongoDB Server
Make sure you install mongodb as a service to run locally as we don't have the option to host our db server on MongoAtlas as stated by this projects SRS
The link to install is below make sure to choose the On-Premise option  
https://www.mongodb.com/try/download/community
Once downloaded install it as a service for less hassle  
If you prefer to do things manually then follow this guide for your respective operating system  
https://www.mongodb.com/docs/manual/administration/install-community/
## ARA client
Either run the GUI.py module or the ARA.exe to open the client
Depending on how populated the library is you will see an amount of books that you can access by clicking
the next screen will then have the book's contents and a place for you to take notes with reminders of SQ3R

## Admin(Easy Insertion of Data)
To insert data into the database use run dbpopulate.py in the terminal with a file as an arguement formatted such that  
line0 = Title  
line1 = Author  
usage: ./dbpopulate.py text1  
some sample texts have been provided, Dune.txt is the most well formatted at the moment

## Contributing
Pull requests are subject to scrutiny

## 422
Please check the GitHub link for the full markdown experience
https://github.com/Aotae/422-projects
