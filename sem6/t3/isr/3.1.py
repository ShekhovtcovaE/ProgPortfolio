from tkinter import *
from tkinter import ttk
import math

def solveEq(a, b, c):  
    d = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(d))  
    
    if d > 0: 
        x1 = (-b + sqrt_val) / (2 * a)
        x2 = (-b - sqrt_val) / (2 * a)
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = x1
    else:    
        x1 = str((- b) / (2 * a)) + ' + i' + str(sqrt_val)
        x2 = str((- b) / (2 * a)) + ' - i' + str(sqrt_val)
    
    return x1, x2

def inserter(value):
    output.delete("0.0","end")
    output.insert("0.0",value)
    

def handler():
    a_val = float(a.get())
    b_val = float(b.get())
    c_val = float(c.get())
    inserter(solveEq(a_val, b_val, c_val))
    

root = Tk()
root.title("Quadratic calculator")
root.minsize(325,230)
root.resizable(width=False, height=False)
 
frame = Frame(root)
frame.grid()

a = Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a_lab = Label(frame, text="x^2 + ").grid(row=1,column=2)
 
b = Entry(frame, width=3)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x + ").grid(row=1, column=4)
 
c = Entry(frame, width=3)
c.grid(row=1, column=5)
c_lab = Label(frame, text=" = 0").grid(row=1, column=6)
 
but = Button(frame, text="Solve", command=handler).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="pink", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()
