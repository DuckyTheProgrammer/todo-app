from cProfile import label
from re import L, template
from tkinter import *
import os
from tkinter import font
from urllib.response import addbase
from tkinter import messagebox

app = Tk()
todoList = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempList = f.read()
        tempList = tempList.split(',')
        todoList = [x for x in tempList if x.strip()]    

def addTodo():


    for widget in listFrame.winfo_children():
        widget.destroy()

    recivedTodo = todoEntry.get()
        
    print(recivedTodo)
    print(todoList)

    todoList.append(recivedTodo)
    for list in todoList:
            todoLabel = Label(listFrame, text=list, bg="gray", fg="white")
            todoLabel.pack()
        


    todoEntry.delete(0, END)


appCanvas = Canvas(app, width=350, height=500, bg="white")
appCanvas.pack()


titleLabel = Label(app, text="TODO LIST APP", bg="white", fg="black", font=10)
titleLabel.place(relwidth=0.5, relheight=0.03, relx=0.25, rely=0.03)

listFrame = Frame(app, bg="#263D42")
listFrame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

addBtn = Button(app, text="Add to do", width=20, height=2,command=addTodo)
addBtn.place(relx=0.3, rely=0.9)

entryLabel = Label(app, text="ENTER TODO:", bg="#263D42", fg="white")
entryLabel.configure(font=("", 8, ""))
entryLabel.place(relwidth=0.3, relheight=0.03, relx=0.1  , rely=0.801)

todoEntry = Entry(app)
todoEntry.place(relheight=0.04,relwidth=0.4,relx=0.4, rely=0.8)


for list in todoList:
    label = Label(listFrame, text= list)
    label.pack()

app.mainloop()

with open('save.txt', 'w') as f:
    for list in todoList:
        f.write(list + ',')