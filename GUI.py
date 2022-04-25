import tkinter
import MDBClient
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from functools import partial

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
    def insert_content(self,text):
        text.insert(INSERT,self.text)
        return

class Notes():
    """
    notes class which contains elements:
    text: the body of the notes
    suggest: the suggestions that will appear in the notes/ styling of structure
    """
    def __init__(self,notes,SQ3R=False):
        self.text = notes
        self.suggest = SQ3R
    def insert_SQ3R(self):
        if(self.suggest):
            for i in range(1,26):
                self.text.insert(f"{i}.0","\n")
            self.text.insert("1.0","You have opted into SQ3R guided note taking")
            self.text.insert("5.0","//01) Remember to survey the book for major topics and ideas")
            self.text.insert("7.0","//02) Next ask yourself Questions on the major topics and ideas that you surveyed")
            self.text.insert("9.0","//03) Once you have some questions in mind it's time to take some notes on the book")
            self.text.insert("19.0","//04) Read your notes to yourself (recite) to help you remember the content")
            self.text.insert("21.0","//05) Finally once you're done looking over your notes try quizing yourself without their help!")
            self.text.insert("23.0","//06) hint press the hide button.")
            self.text.insert("25.0","//07) You can disable this message by simply deleting it or by pressing the SQ3R button again")
            self.text.insert("27.0","//08) Be warned though if you get rid of the message by pressing SQ3R it will delete the lines 1-30 and only leave the chapter title and book title")
            self.suggest = False
        else:
            self.text.delete("1.0","30.0")
            for i in range(1,3):
                self.text.insert(f"{i}.0","\n")
            self.text.insert("2.0","Book Title:")
            self.text.insert("3.0","Chapter Title:")
            self.suggest = True


# https://codingshiksha.com/python/python-3-tkinter-adding-line-numbers-to-text-widget-in-gui-desktop-app-full-project-for-beginners/
# line number class used in this project with minor adjustments
# essentially waits for keypresses and checks if a character was '\n' and increments the line number
# modifications: line number scrolls with the scrollbar associated with our notes text object
class LineNumbers(Text):
    def __init__(self, master, text_widget,note_book_scrl, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(height=100,
                       bg='#bec2cc',
                       yscrollcommand=note_book_scrl.set,
                       padx=0,
                       pady=10,
                       bd=5)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyPress>', self.on_key_press)
        self.configure(state='disabled')
 
    def on_key_press(self, event=None):
        final_index = str(self.text_widget.index(END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))
 
        self.configure(state='normal', width=width)
        self.delete(1.0, END)
        self.insert(1.0, line_numbers_string)
        self.configure(state='disabled')
 
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
        self.protocol('WM_DELETE_WINDOW', lambda:self.exit(False,False,innotes=False,SQ3R=False))
        frame.pack(anchor="nw")
        # for every book in the database display a book button
        # Get all books from db using MDBClient module probably a func like findall
        library = MDBClient.get_library()
        for title in library:
            book_name = title["name"]
            book_content = title["content"]
            book_author = title["author"]
            book = Book(book_name,book_author,book_content)

            book_button = Button(
            frame,
            text = book.name,
            command= partial(self.__new_window,frame,book),
            height = 10,
            width = 15,
            bg = "#79dde8"
            )
            #print(book.name)

            book_button.pack(anchor="nw",side=LEFT,padx=5,pady=5)
        
    def exit(self,notes,book,innotes,SQ3R):
        if messagebox.askokcancel('exit?', 'Are you sure you want to exit?'):
            if(innotes):
                self.note_save(notes,book,SQ3R)
            self.destroy()

    def __new_window(self,frame,book):
        for widgets in frame.winfo_children():
            widgets.destroy()
        frame.destroy()
        # window controller
        self.switch_to_note(book)

    def switch_to_note(self,book):
        #
        #Sets up the note taking window on the right hand side
        #
        self.title("Notebook")
        # get the notes from the database
        notebook_doc = MDBClient.get_notes({"book":book.name})
        if(notebook_doc != None):
            note_content = notebook_doc["notes"]
            print(notebook_doc)
            print("\n")
            print(note_content)
        else:
            note_content= None
        frame = PanedWindow(self,bg="#6699CC",handlesize=16,handlepad=16)
        content_frame = Frame(frame,width=100,height=100,padx=10,bg='#424549',)
        note_frame = Frame(frame,width=165,height=100,padx=10,bg='#424549')
        frame.pack()
        frame.configure(sashrelief = RAISED)
        content_frame.pack(side=LEFT, anchor='ne',expand=True)
        note_frame.pack(side=RIGHT,anchor='nw',expand=True)
        frame.add(content_frame)
        frame.add(note_frame)

        note_book_scrl = Scrollbar(note_frame)
        note_book_scrl.pack(side=RIGHT,fill=Y)
        note_book = Notes(Text(note_frame,
                               width=90,
                               height=100,
                               bg='#bec2cc',
                               yscrollcommand=note_book_scrl.set,
                               padx=10,
                               pady=10,
                               bd=5),True)
        note_book.text.pack(side=RIGHT,padx=5,pady=5,anchor='nw')
        line_number = LineNumbers(note_frame,note_book.text,note_book_scrl,width=1)
        line_number.pack(side=RIGHT,padx=5,pady=5,anchor='nw')
        note_book_scrl.config(command=note_book.text.yview)
        if(note_content == None):
            for i in range(1,3):
                note_book.text.insert(f"{i}.0","\n")
            note_book.text.insert("2.0","Book Title:")
            note_book.text.insert("3.0","Chapter Title:")
        else:
            note_book.text.insert(INSERT,note_content)
            note_book.suggest = not note_book.suggest
        #
        #Sets up the book/content window
        #
        content_scrl = Scrollbar(content_frame)
        content_scrl.pack(side=RIGHT,fill=Y)
        content = Text(content_frame,
                       width=100,
                       height=100,
                       bg= '#EAFFD5',
                       yscrollcommand=content_scrl.set,
                       padx=10,
                       pady=10,
                       bd=5)

        content.pack(side=RIGHT,padx=5,pady=5,anchor='nw')
        content_scrl.config(command=content.yview)

        book.insert_content(content)
        content.config(state=DISABLED)
        
        #
        #Sets up button UI for saving and exiting
        #
        buttonframe = Frame(note_frame,width=20,height=20,bg='#7289da')
        buttonframe.pack(anchor='ne',side=RIGHT)
        save = Button(buttonframe,
            text = 'save',
            command= lambda:self.note_save(note_book.text,book.name,note_book.suggest),
            height = 5,
            width = 5,
            bg = "#7289da")
        save.pack(side=RIGHT,anchor='ne',expand=True)
        finish = Button(buttonframe,
            text = 'finish',
            command= lambda:self.note_finish(note_book.text,book.name,frame,note_book.suggest),
            height = 5,
            width = 5,
            bg = "#7289da")
        finish.pack(side=RIGHT,anchor='ne',expand=True)
        delete = Button(buttonframe,
            text = 'delete',
            command= lambda:self.note_delete(book.name),
            height = 5,
            width = 5,
            bg = "#7289da")
        delete.pack(side=RIGHT,anchor='ne',expand=True)
        hide = Button(buttonframe,
            text = 'hide',
            command= lambda:self.note_finish(note_book.text,book.name,frame),
            height = 5,
            width = 5,
            bg = "#7289da")
        hide.pack(side=RIGHT,anchor='ne',expand=True)
        enableSQ3R = Button(buttonframe,
            text = 'SQ3R',
            command= note_book.insert_SQ3R,
            height = 5,
            width = 5,
            bg = "#7289da")
        enableSQ3R.pack(side=RIGHT,anchor='ne',expand=True)
        self.protocol('WM_DELETE_WINDOW', lambda:self.exit(note_book.text,book.name,innotes=True, SQ3R=note_book.suggest))

    def note_save(self,notes,book_name,SQ3R):
        #saves your notes
        note = {"book":book_name,"notes":notes.get('1.0','end'),"SQ3R":SQ3R}
        if(MDBClient.note_exists({"book":book_name})):
            MDBClient.update({"book":book_name},note)
        else:
            MDBClient.insert_notes(note)
    def note_finish(self,notes,book_name,frame,SQ3R):
        #bring back to library screen after saving
        self.note_save(notes,book_name,SQ3R)
        print(MDBClient.get_notes({"book":book_name}))
        for widgets in frame.winfo_children():
            widgets.destroy()
        frame.destroy()
        self.set_init_window()
    def note_delete(book_name):
        MDBClient.delete_notes(book_name)
    def note_hide():
        pass


if __name__ == "__main__":

    SQ3R = GUI()
    SQ3R.mainloop()
    #MDBClient.delete_library()
    #for testing purposes
    #MDBClient.delete_note_library()
