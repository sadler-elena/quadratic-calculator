from tkinter import *
import math

#Creating GUI:

#Initiating window.
window = Tk()
window.geometry('1920x1080')
#Putting title.
window.title("Quadratic Calculator")

#Defining function to handle "clicked event":
def calculate():
    enterButton.configure(text="Calculate")
    a = int(aEntry.get())
    b = int(bEntry.get())
    c = int(cEntry.get())
    #Calculate discriminant:
    d = (b ** 2) - (4 * a * c)

    if d < 0:
        solutionDescription = Label(window, text='This equation has no real solutions')
        solutionDescription.grid(column=0, row=7)
    if d == 0:
        sol1 = (-b + math.sqrt(d)) / (2 * a)
        solutionDescription = Label(window, text='This equation has one real solution: ' + sol1)
        solutionDescription.grid(column=0, row=7)
    if d > 0:
        sol1 = (-b + math.sqrt(d)) / (2 * a)
        sol2 = (-b - math.sqrt(d)) / (2 * a)
        round(sol1)
        round(sol2)
        sol1 = sol1 * -1
        sol2 = sol2 * -1
        solutionDescription = Label(window,text='The solutions are: ' + str(sol1) + " and " + str(sol2))
        solutionDescription.grid(column=0,row=7)

#Button
enterButton = Button(window, text="Calculate", bg="red", fg="white",command=calculate)


#A
aDescription = Label(window,text="A", font=("Comic Sans", 25))
aEntry = Entry(window,width=10)


#B
bDescription = Label(window,text="B", font=("Comic Sans", 25))
bEntry = Entry(window,width=10)

#C
cDescription = Label(window,text="C", font=("Comic Sans", 25))
cEntry = Entry(window,width=10)


#Adding labels.
description = Label(window, text="Welcome to the quadratic calculator. Please enter your input, then press the calculate button.", font=("Comic Sans", 25))
description2 = Label(window, text="Follow standard equation: ax^2 + bx + c ", font=("Comic Sans", 20))
#Calling function.
description.grid(column=0, row=0)
description2.grid(column=0,row=1)

aDescription.grid(column=0,row=2)
bDescription.grid(column=0,row=3)
cDescription.grid(column=0,row=4)

aEntry.grid(column=1,row=2)
bEntry.grid(column=1,row=3)
cEntry.grid(column=1,row=4)

enterButton.grid(column=0,row=6)
window.mainloop()
