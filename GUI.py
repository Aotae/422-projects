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
    def __init__(self,button,name,content):
        self.button = button
        self.name = name
        self.text = content


class Notes():
    """
    notes class which contains elements:
    text: the body of the notes
    suggest: the suggestions that will appear in the notes/ styling of structure
    """
    def __init__(self,notes,SQ3R):
        self.text = notes
        self.suggest = SQ3R



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
        for i in range(0,10):
            book_button = Button(
            frame,
            text = "Book",
            command= lambda:self.__new_window(frame),
            height = 10,
            width = 15,
            bg = "#79dde8"
            )
            book = Book(book_button,"book","this is the book content")
            book.button.pack(anchor="nw",side=LEFT,padx=5,pady=5)
        
       


    def exit(self):
        if messagebox.askokcancel('exit?', 'Are you sure you want to exit?'):
            self.destroy()

    def __new_window(self,frame):
        for widgets in frame.winfo_children():
            widgets.destroy()
        frame.destroy()
        self.switch_to_note()

    def survey_save(self):
        survey.destroy()
        self.recover_survey_button.destroy()
        self.switch_to_question()
    #don't use
    def hide(self, frame):
        frame.grid_remove()
        recover_button = Button(winNew, text="SHOW", command=frame.grid)
        recover_button.grid(row=0, column=3)

    def switch_to_question(self):
        #save entry to get input
        self.entryWidgets = []
        #question frame setting
        global question
        question = Frame(winNew, height=2, borderwidth=1, relief='groove')
        question.grid(row=0, column=3, sticky=N + S + W + E)
        request = Label(question, text="Write down your questions about this book")
        request.pack()
        #use loop to build entry
        for i in range(1, 5):
            self.entryWidgets.append(Entry(question))
            q_text = "Q"+str(i)+": "
            Label(question, text=q_text).pack()
            self.entryWidgets[-1].pack()
        #build save and hide button
        save_button = Button(question, text="SAVE", command=self.question_save)
        save_button.pack()
        hide_button = Button(question, text="HIDE", command=question.grid_remove)
        hide_button.pack()
        self.recover_question_button = Button(winNew, text="SHOW", command=question.grid)
        self.recover_question_button.grid(row=0, column=3)

    def question_save(self):
        question.destroy()
        self.recover_question_button.destroy()
        self.switch_to_note()
    #need to fix and use in question_save
    def get_entry(self):
        with open('output.txt', 'w') as out:
            for entry in self.entryWidgets:
                out.write(entry.get() + '\n')
    def switch_to_note(self):
        #note frame setting
        self.title("Notebook")
        self.grid_columnconfigure(0,weight=10)
        self.grid_columnconfigure(1,weight=20)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=30)
        table = Frame(self, height=2, borderwidth=1, relief='groove')
        table.pack()
        labeltb = Label(table, text="Table Of Content", justify=LEFT)
        labeltb.pack(side=TOP)
        # book content
        #bookcontent = Text(self)
        #text1.insert("insert", "booktext")
        #text1.grid(row=0, column=1, sticky=N+S+W+E)
        #scrob1 = Scrollbar(winNew, orient=tkinter.VERTICAL)
        #text1.config(yscrollcommand=scrob1.set, state="disabled")
        #scrob1.config(command=text1.yview)
        #scrob1.grid(row=0, column=2, sticky=N+S+W+E)
        #Label(note, text="Note").pack(side=TOP)

        #text setting
        user_note = Text(table, width=50, height=100)
        user_note.pack(side=RIGHT)
        note_bar = Scrollbar(table, orient=tkinter.VERTICAL)
        user_note.config(yscrollcommand=note_bar.set)
        note_bar.config(command=user_note.yview)
        note_bar.pack(side=LEFT, fill=Y, pady=170)
        #build save and hide button
        save_button = Button(table, text="SAVE", command=lambda:self.note_save(user_note))
        save_button.pack(side=RIGHT)
        hide_button = Button(table, text="HIDE", command=table.grid_remove)
        hide_button.pack(side=RIGHT)
        finish_button = Button(table, text="FINISH", command=lambda:self.note_finish("book_name"))
        finish_button.pack(side=RIGHT)
        #self.recover_note_button = Button(winNew, text="SHOW", command=note.grid)
        #self.recover_note_button.grid(row=0, column=3)

    def note_save(self,notes):
        note = {"book":"book_name","notes":notes.get('1.0','end')}
        MDBClient.insert_notes(note)

    def note_finish(self,id):
        print(MDBClient.get_notes({"book":id}))

    def switch_to_review(self):
        global review
        review = Toplevel(self)
        review.geometry(wm_val)
        review.title('Review')


if __name__ == "__main__":
    SQ3R = GUI()
    SQ3R.mainloop()