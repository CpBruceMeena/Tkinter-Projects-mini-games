from tkinter import *
import parser
from math import factorial

root = Tk()
root.title("Calculator")

#get the uses input and place it in the text field
i=0

#defining the function definitions

def get_variable(number):
    global i
    display.insert(i,number)
    i+=1
    
def clear_all():
    display.delete(0,END)
    
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")
        
def get_operator(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

def calculate():
    entire_string = display.get()
    if entire_string[-1]=='!':
        fact()
    else:
        try:
            a = parser.expr(entire_string).compile()
            result = eval(a)
            clear_all()
            display.insert(0,result)
        except Exception:
            clear_all()
            display.insert(0,"Error")

def fact():    
    a = display.get()
    a = a[:-1]
    result = factorial(int(a))
    clear_all()
    display.insert(0,result)
#Adding the input field

display = Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

#Adding the buttons

Button(root,text = "1", command = lambda:get_variable(1)).grid(row=2,column=0)
Button(root,text = "2", command = lambda:get_variable(2)).grid(row=2,column=1)
Button(root,text = "3", command = lambda:get_variable(3)).grid(row=2,column=2)
Button(root,text = "4", command = lambda:get_variable(4)).grid(row=3,column=0)
Button(root,text = "5", command = lambda:get_variable(5)).grid(row=3,column=1)
Button(root,text = "6", command = lambda:get_variable(6)).grid(row=3,column=2)
Button(root,text = "7", command = lambda:get_variable(7)).grid(row=4,column=0)
Button(root,text = "8", command = lambda:get_variable(8)).grid(row=4,column=1)
Button(root,text = "9", command = lambda:get_variable(9)).grid(row=4,column=2)

#Adding another buttons

Button(root,text = "AC", command = lambda:clear_all()).grid(row=5,column=0)
Button(root,text = "0", command = lambda:get_variable(0)).grid(row=5,column=1)
Button(root,text = "=",command=lambda:calculate()).grid(row=5,column=2)

#Adding operators buttons

Button(root,text = "+",command=lambda: get_operator("+")).grid(row=2,column=3)
Button(root,text = "-",command=lambda: get_operator("-")).grid(row=3,column=3)
Button(root,text = "*",command=lambda: get_operator("*")).grid(row=4,column=3)
Button(root,text = "/",command=lambda: get_operator("/")).grid(row=5,column=3)

#Adding other scientific number

Button(root,text = "pi",command=lambda: get_operator("*3.14")).grid(row=2,column=4)
Button(root,text = "%",command=lambda: get_operator("%")).grid(row=3,column=4)
Button(root,text = "(",command=lambda: get_operator("(")).grid(row=4,column=4)
Button(root,text = "exp",command=lambda: get_operator("**")).grid(row=5,column=4)

#Other operations 

Button(root,text = "<-",command=lambda: undo()).grid(row=2,column=5)
Button(root,text = "x!",command=lambda: get_operator("!")).grid(row=3,column=5)
Button(root,text = ")",command=lambda: get_operator(")")).grid(row=4,column=5)
Button(root,text = "^2",command=lambda: get_operator("**2 ")).grid(row=5,column=5)


root.mainloop()
 