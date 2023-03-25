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


# Bottom Description Box
box = tk.Canvas(root, width=1000, height=70, bg="#315887")
box.pack(side="bottom", fill="x")

# Labels are set inside the description box
label1 = tk.Label(box, text="Wind", font=("Poppins",15,'bold'),fg="white", bg="#315887", padx=10, pady=10)
label1.place(relx=0.1, rely=0.5, anchor="w")

label2 = tk.Label(box, text="Air Quality", font=("Poppins",15,'bold'),fg="white", bg="#315887",padx=10, pady=10)
label2.place(relx=0.3, rely=0.5, anchor="w")

label3 = tk.Label(box, text="Description", font=("Poppins",15,'bold'),fg="white", bg="#315887",padx=10, pady=10)
label3.place(relx=0.5, rely=0.5, anchor="w")

label4 = tk.Label(box, text="Air Pressure", font=("Poppins",15,'bold'),fg="white", bg="#315887",padx=10, pady=10)
label4.place(relx=0.7, rely=0.5, anchor="w")

label5 = tk.Label(box, text="Rain", font=("Poppins",15,'bold'),fg="white", bg="#315887",padx=10, pady=10)
label5.place(relx=0.9, rely=0.5, anchor="w")


root.mainloop()