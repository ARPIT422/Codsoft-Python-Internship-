import tkinter as tk
import sqlite3 as sql
from tkinter import ttk
from tkinter import messagebox

#Create an empty list
tasks = []
# Now add task to the list 
def add_task():
    task_string = task_field.get() #the field in which the task is written by the user
    if len(task_string) == 0: 
        messagebox.showinfo('Error', 'Field is empty') #this line of code show the dialog box that field is empty
        print("error")
    else:
        tasks.append(task_string)
        # using the execute () method to store the task in the database.
        the_cursor.execute('insert into tasks values(?)',(task_string,))
        #calling the update functionn to update the list
        list_update()
        # deleting the entry in the entry field
        task_field.delete(0,"end")

# Now create the Update function to update the list
def list_update():
    # calling the list function to clear the list
    clear_list()
    for task in tasks:
        task_listbox.insert("end",task) #here end specifies the item to be ended in the end of the item
        
#Now create the clear list function
def clear_list():
    #using the delete method to delete all the entries from the list box
    task_listbox.delete(0,'end')      #here 0 specifies the end of the list box and end specifies to delete the items upto last element

# Now creat the function to delete the task from the list
def delete_task():
    try:
        # getting the selected entry from the list box  
        the_value = task_listbox.get(task_listbox.curselection())  
        # checking if the stored value is present in the tasks list  
        if the_value in tasks:  
            # removing the task from the list  
            tasks.remove(the_value)  
            # calling the function to update the list  
            list_update()  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('delete from tasks where title = ?', (the_value,)) 
    except:    
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.') 
              
#Now create the delete all function to delete all the entries from the list
def delete_all():
    message_box = messagebox.askyesno("Delete All","Are you Sure ?")
    if message_box == True:
        while(len(tasks)!=0):
            tasks.pop() 
        the_cursor.execute('Delete from tasks') 
        list_update()
        
# Now create the function to close the application
def close():
    #print(tasks)
    # usinf the destroy() method to close the application
    guiWindow.destroy()

# now Create the fucntion to retrieve the data from the database
def retrieve_database():
    while(len(tasks)!=0):
        tasks.pop()
        # iterating through the rows in the database table
        for row in the_cursor.execute('Select title from the tasks'):
            tasks.append(row[0])

# Now Create the main window the application
if __name__ =='__main__':
    guiWindow = tk.Tk()
    guiWindow.title("To-do List Manager")
    guiWindow.geometry("500x500+750+250")
    guiWindow.resizable(0,0)
    guiWindow.configure(bg = "#FAEBD7")

# Now add the database to the application
the_connection = sql.connect('listOfTasks.db')
the_cursor = the_connection.cursor()  
the_cursor.execute('create table if not exists tasks (title text)') 

# Now create a Frame
header_frame = tk.Frame(guiWindow,bg = "#FAEBD7")
function_frame = tk.Frame(guiWindow,bg = "#FAEBD7") 
listbox_frame = tk.Frame(guiWindow,bg = "#FAEBD7") 

# using the pack() method to place the frames in the application
header_frame.pack(fill = 'both')
function_frame.pack(side = "left", expand = True, fill = "both")
listbox_frame.pack(side = "right", expand = True, fill = "both")


# defining a label using the ttk.Label() widget  
header_label = ttk.Label(  
    header_frame,  
    text = "The To-Do List",  
    font = ("Brush Script MT", "30"),  
    background = "#FAEBD7",  
    foreground = "#8B4513"  
)  
# using the pack() method to place the label in the application  
header_label.pack(padx = 20, pady = 20)  

# defining another label using the ttk.Label() widget  
task_label = ttk.Label(  
    function_frame,  
    text = "Enter the Task:",  
    font = ("Consolas", "11", "bold"),  
    background = "#FAEBD7",  
    foreground = "#000000"  
)  
# using the place() method to place the label in the application  
task_label.place(x = 30, y = 40)  

 # defining an entry field using the ttk.Entry() widget  
task_field = ttk.Entry(  
        function_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
# using the place() method to place the entry field in the application  
task_field.place(x = 30, y = 80)  

# adding buttons to the application using the ttk.Button() widget  
add_button = ttk.Button(  
    function_frame,  
    text = "Add Task",  
    width = 24,  
    command = add_task  
)

del_button = ttk.Button(  
    function_frame,  
    text = "Delete Task",  
    width = 24,  
    command = delete_task  
)  

del_all_button = ttk.Button(  
    function_frame,  
    text = "Delete All Tasks",  
    width = 24,  
    command = delete_all 
)  
exit_button = ttk.Button(  
    function_frame,  
    text = "Exit",  
    width = 24,  
    command = close  
)  

# using the place() method to set the position of the buttons in the application  
add_button.place(x = 30, y = 120)  
del_button.place(x = 30, y = 160)  
del_all_button.place(x = 30, y = 200)  
exit_button.place(x = 30, y = 240) 

# defining a list box using the tk.Listbox() widget  
task_listbox = tk.Listbox(  
    listbox_frame,  
    width = 26,  
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)  
# using the place() method to place the list box in the application  
task_listbox.place(x = 10, y = 20) 

# calling some functions  
retrieve_database()  
list_update()  
# using the mainloop() method to run the application  
guiWindow.mainloop()  
# establishing the connection with database  
the_connection.commit()  
the_cursor.close() 
