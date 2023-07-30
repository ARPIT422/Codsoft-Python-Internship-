#Creating a QUIZ GAME

#importing necessary libraries
import tkinter as tk
import sqlite3 as sql
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

c_q_no = 0
score = 0

#defening questions
question = [
    "Who painted the Mona Lisa?",
    "What is the capital of Brazil?",
    "What is the chemical symbol for gold?",
    "Who wrote the play Romeo and Juliet?",
    "What is the largest ocean in the world?"
  ]
#defining options for the respective question
options = [
    ["Vincent Van Gogh","Pablo Picasso","Leonardo da Vinci"," Claude Monet"],
    ["Rio de Janeiro","Brasília", "Sao Paulo","Salvador"],
    [ "Au","Ag","Fe","Hg"],
    ["William Shakespeare","Oscar Wilde","Jane Austen","Charles Dickens"],
    ["Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean"]
  ]
#answere of the corresponding questions
ans = [2,1,0,0,3]

def show_question():
    q_label.config(text = question[c_q_no])  #updating the text of the question
    for i,option in enumerate(options[c_q_no]):  
        option_ratio[i].config(text = option) #updating the text of the radiobutton label

def submit():
    global score
    global c_q_no
    user_answere = var1.get()
    if user_answere == ans[c_q_no]:
        score = score+1
    c_q_no =  c_q_no+1
    var1.set(-1)
    if c_q_no < len(question):
        show_question()
    else:
        messagebox.showinfo("Quiz score","You score {} out of {}".format(score,len(question)))
# creatinf the window of the application        
guiWindow = tk.Tk()
guiWindow.title("To-do List Manager")
guiWindow.geometry("500x300+750+250")
guiWindow.resizable(0,0)
#guiWindow.configure(bg = "#FAEBD7")

#creating frames 
frame_1 = Frame(guiWindow,background = "black")
frame_2 = Frame(guiWindow,background = "yellow")
frame_3 = Frame(guiWindow,background = "yellow")
frame_4 = Frame(guiWindow,background = "green")

#adjusting frames on the application
frame_1.pack(fill = "both")
frame_2.pack(fill = "both")
frame_3.pack(fill = "both")
frame_4.pack(fill = "both")

label = tk.Label(
    frame_1,
    text = "Quiz Game",
    font = ("Times New Roman",40),
    foreground = "red",
    background = "black"
    )
label.pack(fill = "both")

q_label = tk.Label(
    frame_2,
    text = "",
    font = ("Times New Roman",20),
    background = "yellow"
    )
q_label.pack(side = "left")


var1 = IntVar()
option_ratio =[]
var1.set(-1)
for i in range(0,4):
    r_1 = tk.Radiobutton(
    frame_3,
    text = "",
    font = ("Aerial",10),
    background ="yellow",
    variable = var1,
    value = i
    ) 
    r_1.pack(anchor = "w")
    option_ratio.append(r_1)

but = tk.Button(
    frame_4,
    text = "Next",
    font = ("Times New Roman",20),
    command = submit
    )
but.pack()
show_question()
guiWindow.mainloop()
