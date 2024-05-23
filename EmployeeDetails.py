import os
import tkinter as tk
from tkinter import *

import customtkinter
import yaml
from customtkinter.windows.widgets import ctk_button

import EmployeeManager


def Details(root, id):
    for widget in root.winfo_children():
        widget.destroy()

    # Navbar
    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=50, y=11)

    edit = tk.Label(root, text="Edit", font=("Helvetica", 16), bg="white")
    edit.place(x=830, y=11)

    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))

    strem = open("Config/Employees.yaml")
    dictionary = yaml.safe_load(strem)

    #First Name
    name = tk.Label(root, text="Name:", font=("Helvetica", 16))
    name.place(x=50, y=60)

    namefill = tk.Label(root, text=dictionary["Employees"][id]["First Name"], font=("Helvetica", 16))
    namefill.place(x=60, y=90)

    #Last Name
    surname = tk.Label(root, text="Surname:", font=("Helvetica", 16))
    surname.place(x=210, y=62)

    surnamefill = tk.Label(root, text=dictionary["Employees"][id]["Last Name"], font=("Helvetica", 16))
    surnamefill.place(x=60, y=90)

    #Age
    age = tk.Label(root, text="Age:", font=("Helvetica", 16))
    age.place(x=20, y=11)

    agefill = tk.Label(root, text=dictionary["Employees"][id]["Last Name"], font=("Helvetica", 16))
    agefill.place(x=60, y=90)

    jobtitel = tk.Label(root, text="Job Titel", font=("Helvetica", 16))
    jobtitel.place(x=20, y=11)

    email = tk.Label(root, text="Age", font=("Helvetica", 16))
    email.place(x=20, y=11)

    telephone = tk.Label(root, text="Telephone", font=("Helvetica", 16))
    telephone.place(x=20, y=11)

    country = tk.Label(root, text="Country", font=("Helvetica", 16))
    country.place(x=20, y=11)

    address = tk.Label(root, text="Address", font=("Helvetica", 16))
    address.place(x=20, y=11)

    join = tk.Label(root, text="Age", font=("Helvetica", 16))
    age.place(x=20, y=11)