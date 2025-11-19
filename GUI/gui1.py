from tkinter import *
#ka chai locate garni vanera root is imp
root = Tk()
#creating a label, widget
mylabel1 = Label(root,text="Hello world") #create only
mylabel2 = Label(root,text="How are you") 
mylabel3 = Label(root,text="are you all right") 

def myclick():
    lbl = Label(root,text="Look ! i clicked a button !")
    lbl.grid(row=2,column=2)

mybutton = Button(root,text="Click me !!" , padx=20,pady=20,fg="blue",bg="red",command=myclick)
mybutton.grid(row=1,column=3)



#mylabel1.pack() #balla tasiyera(root ma ) gara basni vayo 
#mylabel2.pack()

mylabel1.grid(row=0,column=1)
mylabel2.grid(row=1,column=0)
mylabel3.grid(row=1,column=1)


root.mainloop()

