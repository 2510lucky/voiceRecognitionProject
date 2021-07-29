import mainAssistant
import threading
from tkinter import *
class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        master.title("My Assistant")
        A = Label(master, text="Here to help you!", bg='red')
        A.pack(side="top")
        #photo = PhotoImage(file = r"C:\Users\lucky\Downloads\MY_ASSISTANT-master\MY_ASSISTANT-master\logo.png")
        a = Button(master, text="Edith!", width=20, border="20", relief="groove",
               command=threading.Thread(target=self.Processo_r).start, bg='blue')
        a.place(relx=0.5, rely=0.5, anchor=CENTER)

    def Processo_r(self):
        mainAssistant.calling()

root = Tk()

app = Window(root)
root.geometry("500x500")
root.mainloop()
