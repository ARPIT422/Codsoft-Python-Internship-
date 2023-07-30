import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

var = ""
A = 0
opp = ""
    
#creating func for number
def but1():
    global var
    var = var+"1"
    the_data.set(var)
def but2():
    global var
    var = var+"2"
    the_data.set(var)
def but3():
    global var
    var = var+"3"
    the_data.set(var)
def but4():
    global var
    var = var+"4"
    the_data.set(var)
def but5():
    global var
    var = var+"5"
    the_data.set(var)
def but6():
    global var
    var = var+"6"
    the_data.set(var)
def but7():
    global var
    var = var+"7"
    the_data.set(var)
def but8():
    global var
    var = var+"8"
    the_data.set(var)
def but9():
    global var
    var = var+"9"
    the_data.set(var)
def but0():
    global var
    var = var+"0"
    the_data.set(var)
    
#creating function for operation
def add():
    global var
    global opp
    global A
    opp = "+"
    var = var+ "+"
    the_data.set(var)
def sub():
    global var
    global opp
    opp = "-"
    var = var+"-"
    the_data.set(var)
def mul():
    global var
    global opp
    opp = "*"
    var = var+"*"
    the_data.set(var)
def div():
    global var
    global opp
    opp = "/"
    var = var+"/"
    the_data.set(var)

def res():
    global var
    global opp
    global A
    var = var.split(opp)
    if opp == "+":
        var = float(var[0])+float(var[1])
        the_data.set(var)
        var = str(var)
    if opp == "-":
        var = float(var[0])-float(var[1])
        the_data.set(var)
        var = str(var)
    if opp == "*":
       var = float(var[0])*float(var[1])
       the_data.set(var)
       var = str(var) 
    if opp == "/":
        var = float(var[0])/float(var[1])
        the_data.set(var)
        var = str(var)

#creating application window for the GUI program.
guiWindow = tk.Tk()
guiWindow.title("Calculator")
guiWindow.geometry("300x210+750+250")
guiWindow.resizable(0,0)
#guiWindow.configure(bg = "#FAEBD7")

frame_1 = tk.Frame(guiWindow,bg = "red")
frame_2 = tk.Frame(guiWindow,bg = "black")
frame_3 = tk.Frame(guiWindow,bg = "red")
frame_4 = tk.Frame(guiWindow,bg = "black")
frame_5 = tk.Frame(guiWindow,bg = "red")
frame_6 = tk.Frame(guiWindow,bg = "black")

frame_1.pack(fill = "both")
frame_2.pack(fill = "both")
frame_3.pack(fill = "both")
frame_4.pack(fill = "both")
frame_5.pack(fill = "both")
frame_6.pack(fill = "both")

#creating widget for frame1
header_label = tk.Label(  
    frame_1,  
    text = "Simple Calculator",  
    font = ("Times New Roman", "25"),  
    background = "sky blue",  
    foreground = "red"  
)  
header_label.pack(fill = "both")  

#creating widget for frame2
the_data = StringVar()  
field = tk.Entry(  
        frame_2, 
        font = ("Times New Roman", "12"),  
        width = 18,  
        textvariable = the_data,   
        border = 15,
    
    )  
field.pack(fill = "both") 

#creating widget for frame3
b7 = ttk.Button(  
    frame_3,  
    text = "7",  
    width = 11,  
    command = but7
)  

b8 = ttk.Button(  
    frame_3,  
    text = "8",  
    width = 11,  
    command = but8
)  

b9 = ttk.Button(  
    frame_3,  
    text = "9",  
    width = 11,  
    command = but9
)  

bC = ttk.Button(  
    frame_3,  
    text = "C",  
    width = 11,  
    #command = 
)  
b7.pack(side = "left")
b8.pack(side = "left")
b9.pack(side = "left")
bC.pack(side = "left")

#creating widget for frame4
b4 = ttk.Button(  
    frame_4,  
    text = "4",  
    width = 11,  
    command = but4
)  

b5 = ttk.Button(  
    frame_4,  
    text = "5",  
    width = 11,  
    command = but5
)  

b6 = ttk.Button(  
    frame_4,  
    text = "6",  
    width = 11,  
    command =but6 
)  

b_add = ttk.Button(  
    frame_4,  
    text = "+",  
    width = 11,  
    command = add
)  
b4.pack(side = "left")
b5.pack(side = "left")
b6.pack(side = "left")
b_add.pack(side = "left")

#creating widget for frame5
b1 = ttk.Button(  
    frame_5,  
    text = "1",  
    width = 11,  
    command = but1
)  

b2 = ttk.Button(  
    frame_5,  
    text = "2",  
    width = 11,  
    command = but2 
)  

b3 = ttk.Button(  
    frame_5,  
    text = "3",  
    width = 11,  
    command = but3
)  

b_sub = ttk.Button(  
    frame_5,  
    text = "-",  
    width = 11,  
    command = sub
)  
b1.pack(side = "left")
b2.pack(side = "left")
b3.pack(side = "left")
b_sub.pack(side = "left")

#creating widget for frame6
b0 = ttk.Button(  
    frame_6,  
    text = "0",  
    width = 11,  
    command = but0
)  

b_mul = ttk.Button(  
    frame_6,  
    text = "*",  
    width = 11,  
    command = mul
)  

b_div = ttk.Button(  
    frame_6,  
    text = "/",  
    width = 11,  
    command =div 
)  

b_equal = ttk.Button(  
    frame_6,  
    text = "=",  
    width = 11,  
    command = res
)  
b0.pack(side = "left")
b_mul.pack(side = "left")
b_div.pack(side = "left")
b_equal.pack(side = "left")

guiWindow.mainloop()

