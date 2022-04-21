import tkinter
from tkinter import *
from tkinter import filedialog, messagebox


class GUI(Tk):

    def __init__(self,):
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
        self.protocol('WM_DELETE_WINDOW', self.exit)
        btn1 = Button(self, text='book1', command=self.__new_window, bg='#d3fbf6', relief=RIDGE)
        btn1.place(relx=0.1, rely=0.1, width=100, height=150)

    def exit(self):
        if messagebox.askokcancel('exit?', 'Are you sure to exit?'):
            self.destroy()

    def __new_window(self):
        #new window setting
        global winNew
        winNew = Toplevel(self)
        winNew.grid_columnconfigure(0, weight=10)
        winNew.grid_columnconfigure(1, weight=20)
        winNew.grid_columnconfigure(2, weight=1)
        winNew.grid_columnconfigure(3, weight=30)
        winNew.grid_rowconfigure(0, weight=1)
        winNew.transient(self)
        winNew.geometry(wm_val)
        winNew.title('Notebook')
        #content setting
        table = Frame(winNew, height=2, borderwidth=1, relief='groove')
        table.grid(row=0, column=0, sticky=N+S+W+E)
        label1 = Label(table, text="Table Of Content", justify=LEFT)
        label1.pack(side=TOP)
        #Text setting
        #booktext = Frame(winNew, height=2, borderwidth=1, relief='groove')
        #booktext.grid(row=0, column=1, sticky=N+S+W+E)
        text1 = Text(winNew)
        text1.insert("insert", "booktext")
        text1.grid(row=0, column=1, sticky=N+S+W+E)
        scrob1 = Scrollbar(winNew, orient=tkinter.VERTICAL)
        text1.config(yscrollcommand=scrob1.set, state="disabled")
        scrob1.config(command=text1.yview)
        scrob1.grid(row=0, column=2, sticky=N+S+W+E)
        #Note setting
        global survery
        survery = Frame(winNew, height=2, borderwidth=1, relief='groove')
        survery.grid(row=0, column=3, sticky=N + S + W + E)
        surv_title = Label(survery, text="Survey", justify=CENTER, font=('Time New Roman', 20, 'bold'))
        surv_title.pack()
        surv_label1 = Label(survery, text="Q1: What do you know about this book?", justify=LEFT)
        surv_label1.pack()
        surv_input1 = Entry(survery, bd=2, width=30)
        surv_input1.pack()
        surv_label2 = Label(survery, text="Q2: What do you want to know from this book?", justify=LEFT)
        surv_label2.pack()
        surv_input2 = Entry(survery, bd=2, width=30)
        surv_input2.pack()
        save_button = Button(survery, text="SAVE", command=self.survery_save)
        save_button.pack()
        hide_button = Button(survery, text="HIDE", command=survery.grid_remove)
        hide_button.pack()
        self.recover_survery_button = Button(winNew, text="SHOW", command=survery.grid)
        self.recover_survery_button.grid(row=0, column=3)


    def survery_save(self):
        survery.destroy()
        self.recover_survery_button.destroy()
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
        global note
        note = Frame(winNew, height=2, borderwidth=1, relief='groove')
        note.grid(row=0, column=3, sticky=N + S + W + E)
        Label(note, text="Note").pack(side=TOP)
        #text setting
        user_note = Text(note, width=100, height=50)
        user_note.pack(side=LEFT)
        note_bar = Scrollbar(note, orient=tkinter.VERTICAL)
        user_note.config(yscrollcommand=note_bar.set)
        note_bar.config(command=user_note.yview)
        note_bar.pack(side=LEFT, fill=Y, pady=170)
        #build save and hide button
        save_button = Button(note, text="SAVE", command=self.note_save)
        save_button.pack(side=BOTTOM)
        hide_button = Button(note, text="HIDE", command=note.grid_remove)
        hide_button.pack(side=BOTTOM)
        finish_button = Button(note, text="FINISH", command=self.note_finish)
        finish_button.pack(side=BOTTOM)
        self.recover_note_button = Button(winNew, text="SHOW", command=note.grid)
        self.recover_note_button.grid(row=0, column=3)

    def note_save(self):
        pass

    def note_finish(self):
        winNew.destroy()
        self.switch_to_review()

    def switch_to_review(self):
        global review
        review = Toplevel(self)
        review.geometry(wm_val)
        review.title('Review')


if __name__ == "__main__":
    SQ3R = GUI()

    SQ3R.mainloop()