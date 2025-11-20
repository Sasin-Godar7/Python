from tkinter import *

root = Tk()
root.title("Entryy Box !")

e = Entry(root,width=50,fg='sky blue',bg='red')
e.pack()
e.insert(0,"Enter your name >")

def myclick():
    mylabel = Label(root,text="hello" + e.get()+"whats up !!")
    mylabel.pack()

btn=Button(root,text="Click me ",command=myclick)
btn.pack()
root.mainloop()
