import tkinter as tk
from tkinter import messagebox
import open

class gui:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("facebook login")
        self.root.geometry("250x150")
        self.root.protocol("WM_DELETE_WINDOW",self.onclose)
        self.root.rowconfigure(0 ,weight=1)
        self.root.rowconfigure(1 ,weight=1)
        self.root.rowconfigure(2 ,weight=1)
        self.l1=tk.Label(self.root,text="Email: ",font=("Roboto",12))
        self.l1.grid(row=0,column=0,sticky=tk.W)
        self.e1=tk.Entry(self.root)
        self.e1.grid(row=0,column=1)
        self.e2=tk.Entry(self.root,show="*")
        self.e2.grid(row=1,column=1)
        self.l2=tk.Label(self.root,text="Password:" ,font=("Roboto",12))
        self.l2.grid(row=1,column=0)
        self.b1=tk.Button(self.root,text="login",font=("Roboto",14),command=self.login)
        self.b1.grid(row=2,column=0,columnspan=2)
        self.root.mainloop()
        
    def onclose(self):
        if messagebox.askyesno(title="close",message="are you sure?"):
            self.root.destroy()

    def login(self):
        user=self.e1.get()
        
        pas=self.e2.get()
        
        open.auto(user,pas)
        
gui()