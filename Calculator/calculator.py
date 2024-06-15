from tkinter import *
import numpy as np
import math

# Function to handle button clicks
def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = scvalue.get()
            
            # Check and handle specific functions
            if "√" in expression:
                number = expression.split("√")[1]
                value = np.sqrt(float(number))
            elif "sin" in expression:
                number = expression.split("sin")[1]
                value = np.sin(np.radians(float(number)))
            elif "cos" in expression:
                number = expression.split("cos")[1]
                value = np.cos(np.radians(float(number)))
            elif "tan" in expression:
                number = expression.split("tan")[1]
                value = np.tan(np.radians(float(number)))
            elif "sinh" in expression:
                number = expression.split("sinh")[1]
                value = np.sinh(float(number))
            elif "cosh" in expression:
                number = expression.split("cosh")[1]
                value = np.cosh(float(number))
            elif "tanh" in expression:
                number = expression.split("tanh")[1]
                value = np.tanh(float(number))
            elif "log" in expression:
                number = expression.split("log")[1]
                value = np.log10(float(number))
            elif "ln" in expression:
                number = expression.split("ln")[1]
                value = np.log(float(number))
            elif "^2" in expression:
                number = expression.split("^2")[0]
                value = float(number) ** 2
            elif "^" in expression:
                base, exponent = expression.split("^")
                value = float(base) ** float(exponent)
            elif "!" in expression:
                number = expression.split("!")[0]
                value = math.factorial(int(number))
            
            elif "1/" in expression:
                number = expression.split("1/")[1]
                value = 1 / float(number)
            
            else:
                value = eval(expression)
        except:
            value = "ERROR"
        scvalue.set(value)
        screen.update()
    
    elif text == "C":
        scvalue.set("")
        screen.update()
    
    elif text == "<-":
        current_value = scvalue.get()
        scvalue.set(current_value[:-1])
        screen.update()
    
    elif text in ("√", "(", ")", "sin", "cos", "tan", "sinh", "cosh", "tanh", "log", "ln", "^2", "^", "!", "1/", "+/-"):
        # Just append the symbol to the current expression
        scvalue.set(scvalue.get() + text)
        screen.update()
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

        
root = Tk()
root.geometry("400x630")
root.title("Calculator in Python")
#root.wm_iconbitmap("")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=10, ipady=15, pady=20, padx=15)
#===========================================================================
f = Frame(root, bg="grey")
b= Button(f, text="(", height=2, width=4 ,font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text=")", height=2, width=4 ,font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="sin", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="cos", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="tan", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()
#==========================================================================

f = Frame(root, bg="grey")
b= Button(f, text="√", height=2, width=4 ,font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="log", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="sinh", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="cosh", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="tanh", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()
#==========================================================================

f = Frame(root, bg="grey")
b= Button(f, text="1/", height=2, width=4 ,font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="%", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="C", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="<-", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="+", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()
#===========================================================================

f = Frame(root, bg="grey")
b= Button(f, text="^", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="7", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="8", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="9", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="-", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()
#==============================================================================

f = Frame(root, bg="grey")
b= Button(f, text="^2", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="4", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="5", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="6", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="*", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()
#=============================================================================

f = Frame(root, bg="grey")
b= Button(f, text="!", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="1", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="2", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="3", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="/", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()
#=============================================================================

f = Frame(root, bg="grey")
b= Button(f, text="ln", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="+/-", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="0", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text=".", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)

b= Button(f, text="=", height=2, width=4, font="lucida 15 bold")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()
#==============================================================================
root.mainloop()