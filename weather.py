from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("1000x600+300+200")
root.resizable(False,False)


# Search Box
# Search_image=PhotoImage(file="")
def search():
    # code to perform search goes here
    search_term = entry.get()
    print(f"Searching for: {search_term}")
# root = tk.Tk()
entry = tk.Entry(root, justify="center", width=30)
entry.pack()
entry.place(x=60, y=40)

button = tk.Button(root, justify="center", text="Search", command=search)
button.pack()
button.place(x=350, y=39)

# Logo
Logo_image=PhotoImage(file="assets/logo.png")
logo=Label(image=Logo_image)
logo.place(x=150, y=100)


# Bottom Box



root.mainloop()