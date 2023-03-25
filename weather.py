from tkinter import *
import tkinter as tk
# from PIL import Image, ImageTk
from PIL import Image,ImageTk
from tkinter import Tk, Label
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
# Original Image Size: 429x368

# load the image
image = Image.open("assets/logo.png")
resized_image= image.resize((329,268), Image.ANTIALIAS)

# convert the resized image to a Tkinter-compatible format
# Note that when using the ImageTk.PhotoImage method,
# the image must be kept as a reference to avoid being garbage collected by Python.
# This means that you need to keep a reference to the tk_image variable in your program,
# for example by assigning it to an attribute of a class or by using a global variable.
tk_image = ImageTk.PhotoImage(resized_image)

# create a label with the image
label = tk.Label(root, image=tk_image)
# Position the Image on canvas
label.place(x=100, y=100)
label.pack()


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


# Code Snippets
# Set Window Icon in Tkinter
# tk.call('wm', 'Iconphoto', ) - Method to Set Window Icon
# root.iconbitmap - to Set Window Icon
# root.iconphoto - to Set Window Icon