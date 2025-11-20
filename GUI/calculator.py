# from tkinter import *
# root = Tk()
# root.title("Calculator !")

# e = Entry(root,width=60,fg='sky blue',bg='black')
# e.pack()
# e.insert(0," calculate me")

# def calculate():
#     mylabel = Label(root, e.get())
#     mylabel.pack()

# btn1=Button(root,text="9" ,command=calculate,width=6,height=4)
# btn2=Button(root,text="8" ,command=calculate)
# btn3=Button(root,text="7" ,command=calculate)
# btn4=Button(root,text="6" ,command=calculate)
# btn5=Button(root,text="5" ,command=calculate)
# btn6=Button(root,text="4" ,command=calculate)
# btn7=Button(root,text="3" ,command=calculate)
# # btn1.grid(row=0,column=0)
# # btn2.grid(row=0,column=1)
# # btn3.grid(row=0,column=3)

# root.mainloop()

from tkinter import *

root = Tk()
root.title("Simple Calculator UI")
root.geometry("300x400")
root.configure(bg="black")

# Display Screen
e = Entry(root, width=20, font=("Arial", 20), border=5, bg="white", fg="black")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


# ----- Buttons -----
btn_text = [
    ["7", "8", "9", "C"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "*"]
]

# Create buttons grid
for r in range(4):
    for c in range(4):
        Button(
            root,
            text=btn_text[r][c],
            padx=20,
            pady=20,
            font=("Arial", 14),
            bg="#222",
            fg="white",
        ).grid(row=r+1, column=c, padx=5, pady=5)

root.mainloop()

