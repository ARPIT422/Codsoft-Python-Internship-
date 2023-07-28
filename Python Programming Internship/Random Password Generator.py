import random as rns
import tkinter as tk
import sqlite3 as sql
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12!@#$^&*-"

def close():
    guiWindow.destroy()

def generate_password():
    a = int(pass_len_field.get()) 
    a = rns.sample(list,a)
    a = ''.join(map(str, a))
    gen_pass_field.delete(0,tk.END)
    gen_pass_field.insert(0,a)
    
def cl():
    user_name_field.delete(0,tk.END)
    pass_len_field.delete(0,tk.END)
    gen_pass_field.delete(0,tk.END)
    
    #the_data.set(a)
#creating application main window
guiWindow =tk.Tk()
guiWindow.title("Random Password Generator Application")
guiWindow.geometry("500x250+750+250")
guiWindow.resizable(0,0)
guiWindow.configure(bg = "black")
# creating frames on the applications
frame_1 = tk.Frame(guiWindow,background = "black")
frame_2 = Frame(guiWindow, width = 200, height = 150,background = "black")
frame_3 = Frame(guiWindow,background = "black")

# adjusting the frames on the window in a specified location
frame_1.pack(fill = "both")
frame_2.pack(fill = "both")
frame_3.pack(fill = "both")

label = Label(
    frame_1,
    text = "Random Password Generator",
    font = ("Times New Roman",30,"bold"),
    foreground = ("white"),
    background = "black"
    )
label.pack(fill = "both")

user = Label(
    frame_2,
    text = "User Name",
    font = ("Times New Roman",20),
    foreground = "red",
    background = "black"
    )
user.place(x=0,y=10 )

user_name_field = Entry(
    frame_2, 
    )
user_name_field.place(x=150,y = 20)

pass_len = Label(
    frame_2,
    text = "Password Length Field",
    font = ("Times New Roman",20),
    foreground = "red",
    background = "black"
    )
pass_len.place(x=0,y=50 )

pass_len_field = Entry(
    frame_2
    )
pass_len_field.place(x=280,y=60)

gen_pass = Label(
    frame_2,
    text = "Gen. Password",
    font = 20,
    foreground = "red",
    background = "black"
    )
gen_pass.place(x=0,y=90 )

#the_data = StringVar()
gen_pass_field = Entry(
    frame_2,
    highlightbackground="blue",
   # textvariable = the_data
    )
gen_pass_field.place(x=160,y=100)

clear= Button(
    frame_3,
    text = "Reset",
    font = 20,
    command = cl
    )
clear.pack(side = "left",padx = 20)

gen_pass_btn= Button(
    frame_3,
    text = "Generate Password",
    font = 20,
    command = generate_password
    )
gen_pass_btn.pack(side = "left",padx = 40)

exit= Button(
    frame_3,
    text = "Exit",
    font = 20,
    command = close
    )
exit.pack(side = "left",padx =40)
guiWindow.mainloop()
