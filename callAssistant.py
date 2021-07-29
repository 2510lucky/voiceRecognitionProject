import mainAssistant
import threading
import tkinter.font as font
from tkinter import *

class Window(Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.pack()
        master.title("My Assistant")

        buttonFont1 = font.Font(family='Helvetica', size=16, weight='bold')

        A = Label(master, text="Here to help you!",
                  bg='yellow', font=buttonFont1)
        A.pack(side="top")

        buttonFont2 = font.Font(family='Helvetica', size=20, weight='bold')
        a = Button(master, text="Edith!", width=20, border="20", relief="groove", command=threading.Thread(target=self.Processo_r).start, bg='blue', font=buttonFont2)
        a.place(relx=0.5, rely=0.5, anchor=CENTER)

        b = Button(master, text="Stop", width=10, border="50", relief="groove", command=root.destroy, bg='red', font=buttonFont2)
        b.place(relx=0.5, rely=0.8, anchor=CENTER)

    def Processo_r(self):
        mainAssistant.calling()

root = Tk()

app = Window(root)
root.geometry("500x500")
root.configure(bg='black')
root.mainloop()
