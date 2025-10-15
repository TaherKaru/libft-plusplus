from tkinter import *

window = Tk()
window.title("Basic Calculator")
window.geometry("392x400")
window.maxsize(392,400)

# entry box
e = Entry(window, width=58, border=10)
e.place(x=10, y=0)

# buttons

def click (num):
    result=e.get()
    e.delete(0,END)
    e.insert(END,str(result) + str(num))

b = Button(window, text="1", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(1))
b.place(x=20, y=80)

b = Button(window, text="2", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(2))
b.place(x=110, y=80)

b = Button(window, text="3", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(3))
b.place(x=200, y=80)

#-----------------------------------------------------------------------------------------------------------------------

def clear():
    e.delete(0,END)

b = Button(window, text="DEL", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8 ,command=clear)
b.place(x=290, y=80)

#-----------------------------------------------------------------------------------------------------------------------

b = Button(window, text="4", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(4))
b.place(x=20, y=150)

b = Button(window, text="5", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(5))
b.place(x=110, y=150)

b = Button(window, text="6", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(6))
b.place(x=200, y=150)
#-----------------------------------------------------------------------------------------------------------------------
def add():
    n1=e.get()
    global math
    math = "addition"
    global i
    i=int(n1)
    e.delete(0,END)

b = Button(window, text="+", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=add)
b.place(x=290, y=150)

#-----------------------------------------------------------------------------------------------------------------------

b = Button(window, text="7", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(7))
b.place(x=20, y=220)

b = Button(window, text="8", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(8))
b.place(x=110, y=220)

b = Button(window, text="9", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(9))
b.place(x=200, y=220)
#-----------------------------------------------------------------------------------------------------------------------
def sub():
    n1=e.get()
    global math
    math = "subtraction"
    global i
    i=int(n1)
    e.delete(0,END)


b = Button(window, text="-", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=sub)
b.place(x=290, y=220)

#-----------------------------------------------------------------------------------------------------------------------
b = Button(window, text="0", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=lambda:click(0))
b.place(x=20, y=290)
#-----------------------------------------------------------------------------------------------------------------------

def div():
    n1=e.get()
    global math
    math = "division"
    global i
    i=int(n1)
    e.delete(0,END)

b = Button(window, text="/", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=div)
b.place(x=110, y=290)

#-----------------------------------------------------------------------------------------------------------------------

def mul():
    n1=e.get()
    global math
    math = "multiplication"
    global i
    i=int(n1)
    e.delete(0,END)

b = Button(window, text="*", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8,command=mul)
b.place(x=200, y=290)

#-----------------------------------------------------------------------------------------------------------------------
def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))

b = Button(window, text="=", fg="red", bg="aqua", activebackground="grey", border=5, height=2, width=8 , command=equal)
b.place(x=290, y=290)

window.mainloop()
