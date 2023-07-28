#import necessary libraries
import kaggle
import os
import subprocess
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import tkinter as tk
import sqlite3 as sql
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pandas as pd

os.environ['KAGGLE_USERNAME'] = 'arpitbansal409'
os.environ['KAGGLE_KEY'] = '13600b4d0863a9474b89484596e1eb55'
subprocess.run(['kaggle', 'datasets', 'download', '-d', 'arpitbansal409/weather-forecast-data'])

# download the dataset to local machine in a specified location
with zipfile.ZipFile('weather-forecast-data.zip', 'r') as zip_ref:
    zip_ref.extractall('C:/Users/HP/Desktop/python')

#load the download    
df = pd.read_csv(r"C:\Users\HP\Desktop\python\weather forecast data.csv")
city = df["City"].tolist()
zipcode = df["Zipcode"].tolist()
temperature = df["Temperature (°C)"].tolist()
hummidity = df["Humidity (%)"].tolist()
windspeed = df["Wind Speed (km/h)"].tolist()

#creating fuction that gives the temperature, hummidity and windspeed of a pariticular city
def show():
    c_name = city_name_field.get()
    z_code = zip_code_field.get()
    z_code = int(z_code)
    if (c_name in city and z_code in zipcode):
         i = city.index(c_name)
         j = zipcode.index(z_code)
         if(i==j):
             the_data_1.set(temperature[i]) 
             the_data_2.set(hummidity[i])
             the_data_3.set(windspeed[i]) 
         else: 
            messagebox.showinfo("error","Zip-Code corresponding to City is not matched")
    else:
        messagebox.showinfo("Error","The city you entered not exist in the database")
def close():
    guiWindow.destroy()
    
#creating application main window
guiWindow =tk.Tk()
guiWindow.title("Weather Forecast Application")
guiWindow.geometry("500x350+750+250")
guiWindow.resizable(0,0)

# creating frames on the applications
frame_1 = tk.Frame(guiWindow,background = "black")
frame_2 = Frame(guiWindow, width = 200, height = 220, background = "blue")
frame_3 = Frame(guiWindow)
frame_4 = Frame(guiWindow)
frame_5 = Frame(guiWindow)

# adjusting the frames on the window in a specified location
frame_1.pack(fill = "both")
frame_2.pack(fill = "both")
frame_3.pack(fill = "both")
frame_4.pack(fill = "both")
frame_5.pack(fill = "both")

#creating widgets for the application
label = Label(
    frame_1,
    text = "Weather Forecast Application",
    font = ("Times New Roman",30)
    )
label.pack(fill = "both")

city_name = Label(
    frame_2,
    text = "City Name",
    font = 20
    )
city_name.place(x=0,y=10 )

zip_code = Label(
    frame_2,
    text = "Zip Code",
    font = 20
    )
zip_code.place(x=0,y=50 )

temp = Label(
    frame_2,
    text = "Temperature",
    font = 20
    )
temp.place(x=0,y=90 )

humd = Label(
    frame_2,
    text = "Humdidity %",
    font = 20
    )
humd.place(x=0,y=130 )

wind_speed = Label(
    frame_2,
    text = "Wind speed \n (Km/hrs)",
    font = 20
    )
wind_speed.place(x=0,y=170 )

city_name_field = Entry(
    frame_2
    )
city_name_field.place(x=120,y = 10)

zip_code_field = Entry(
    frame_2
    )
zip_code_field.place(x=120,y=50)

the_data_1 = StringVar()
temp_field = Entry(
    frame_2,
    textvariable = the_data_1
    #text = "SS"
    )
temp_field.place(x=120,y=90)

the_data_2 = StringVar()
hum_field = Entry(
    frame_2,
    textvariable = the_data_2
    )
hum_field.place(x=120,y=130)

the_data_3 = StringVar()
wind_speed_field = Entry(
    frame_2,
    textvariable = the_data_3
    )
wind_speed_field.place(x=120,y=170)


show = Button(
    frame_5,
    text = "Show",
    font = 20,
    command = show
    )
show.pack(side = "left")

exit =Button(frame_5,
               text = "Exit",
               font = 20,
               command = close
               ) 
exit.pack(side = "left")
guiWindow.mainloop()