import tkinter
import MDBClient
from tkinter import *
from tkinter import filedialog, messagebox

class Book():
    """
    Book class which contains elements:
    button: a button to select the book from the library screen
    name: the name of the book
    text: the contents of the book
    """
    def __init__(self,name,author,content):
        self.name = name
        self.text = content
        self.author = author


class Notes():
    """
    notes class which contains elements:
    text: the body of the notes
    suggest: the suggestions that will appear in the notes/ styling of structure
    """
    def __init__(self,notes,SQ3R):
        self.text = notes
        self.suggest = SQ3R
    def insert_SQ3R(self):
        if(self.suggest):
            self.text.insert(INSERT,"You have opted into SQ3R guided note taking\n\n")
            self.text.insert(INSERT,"//01) Remember to survey the book for major topics and ideas\n\n")
            self.text.insert(INSERT,"//02) Next ask yourself Questions on the major topics and ideas that you surveyed\n\n")
            self.text.insert(INSERT,"//03) Once you have some questions in mind it's time to take some notes on the book\n//\n//\n//\n//\n//\n//\n//\n")
            self.text.insert(INSERT,"//04) Read your notes to yourself (recite) to help you remember the content\n\n")
            self.text.insert(INSERT,"//05) Finally once you're done looking over your notes try quizing yourself without their help! \n hint press the hide button.\n\n")
    def remove_SQ3R(self):
        #clears the text box
            if(self.suggest):
                self.text.delete(0,end)





class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.frames = {}
        self.set_init_window()

    def set_init_window(self):
        self.title("Bookcase")
        global scn_width, scn_height
        scn_width, scn_height = self.maxsize()
        global wm_val
        wm_val = '1980x1024+{}+{}'.format((scn_width - 1980) // 2, (scn_height - 1024) // 2)
        self.geometry(wm_val)
        frame = Frame(self,bg="#f2d7b1")
        frame.pack(anchor="nw")
        self.protocol('WM_DELETE_WINDOW', self.exit)
        # for every book in the database display a book button
        # Get all books from db using MDBClient module probably a func like findall
        library = MDBClient.get_library()
        for title in library:
            book_name = title["name"]
            book_content = title["content"]
            book_author = title["author"]
            book = Book(book_name,book_content,book_author)

            book_button = Button(
            frame,
            text = book.name,
            command= lambda:self.__new_window(frame,book),
            height = 10,
            width = 15,
            bg = "#79dde8"
            )

            book_button.pack(anchor="nw",side=LEFT,padx=5,pady=5)
        
       


    def exit(self):
        if messagebox.askokcancel('exit?', 'Are you sure you want to exit?'):
            self.destroy()

    def __new_window(self,frame,book):
        for widgets in frame.winfo_children():
            widgets.destroy()
        frame.destroy()
        # window controller
        self.switch_to_note(book)

    def switch_to_note(self,book):
        #Sets up the note taking window on the right hand side
        self.title("Notebook")
        frame = Frame(self,bg="#F8F0E3")
        book_frame = Frame(self,bg="#F8F0E3")
        frame.pack(anchor='ne')
        book_frame.pack(anchor='nw')

        note_book_scrl = Scrollbar(frame)
        note_book_scrl.pack(side=RIGHT,fill=Y)
        note_book = Notes(Text(frame,width=100,
                               height=100,
                               bg='#bec2cc',
                               yscrollcommand=note_book_scrl.set,
                               padx=10,
                               pady=10,
                               bd=5),True)
        note_book.text.pack(anchor='ne',fill=BOTH)
        note_book_scrl.config(command=note_book.text.yview)
        note_book.insert_SQ3R()
        #Sets up the book/content window
        content_scrl = Scrollbar(book_frame)
        content_scrl.pack(side=RIGHT,fill=Y)
        content = Text(book_frame,
                       width=100,
                       height=100,
                       bg= '#F8F0E3',
                       yscrollcommand=content_scrl.set,
                       padx=10,
                       pady=10,
                       bd=5)
        content.insert(INSERT,book.text)
        content.pack(anchor='nw',fill=BOTH)
        content_scrl.config(command=content.yview)

    def note_save(self,notes,book_name):
        note = {"book":book_name,"notes":notes.get('1.0','end')}
        MDBClient.insert_notes(note)
    def note_finish(self,id):
        print(MDBClient.get_notes({"book":id}))


if __name__ == "__main__":

    MDBClient.insert_books({"name":"DUNE","content":"This is the book Dune,\n We don't have the license to it so filler text\n","author":"Frank Herbert"})
    MDBClient.insert_books({"name":"DUNE1","content":"This is the book Dune,\n We don't have the license to it so filler text\n","author":"Frank Herbert"})
    MDBClient.insert_books({"name":"DUNE2","content":"This is the book Dune,\n We don't have the license to it so filler text\n","author":"Frank Herbert"})
    MDBClient.insert_books({"name":"DUNE3","content":"This is the book Dune,\n We don't have the license to it so filler text\n","author":"Frank Herbert"})
    SQ3R = GUI()
    SQ3R.mainloop()
