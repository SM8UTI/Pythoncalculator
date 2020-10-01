from tkinter import *

"""
author      : Smruti Ranjan Nayak
Github Link : https://github.com/SmrutiRN
"""

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    value = ""
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

    elif text!="c":
        value = scvalue.get()+ text

    scvalue.set(value)
    screen.update()

root = Tk()
root.geometry("600x900")
root.title("Calculator")
root.config(bg="orange")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


for i in range(9 ,0, -3):
    f = Frame(root, bg="grey")
    
    for i in range(i, i-3, -1):
        b = Button(f, text=str(i), padx=10, pady=5, font="lucida 35 bold")
        b.pack(side=LEFT, padx=10, pady=5)
        b.bind("<Button-1>", click)
        
    f.pack()


f = Frame(root, bg="grey")

for char in "0-*":
    b = Button(f, text=char, padx=10, pady=5, font="lucida 35 bold")
    b.pack(side=LEFT, padx=13, pady=5)
    b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

for char in "/%=":
    b = Button(f, text=char, padx=10, pady=5, font="lucida 35 bold")
    b.pack(side=LEFT, padx=9, pady=5)
    b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="c", padx=10, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="clac", padx=10, pady=5, font="lucida 25 bold")
b.pack(side=LEFT, padx=5, pady=5)


b = Button(f, text="+", padx=10, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()









