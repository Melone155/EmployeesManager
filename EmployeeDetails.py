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
    back.place(x=20, y=11)

    add = tk.Label(root, text="Add", font=("Helvetica", 16), bg="white")
    add.grid(row=0, column=1, sticky='e', padx=20)

    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))

    #Body
    name = tk.Label(root, text="Name:", font=("Helvetica", 16), bg="white")
    name.place(x=20, y=11)

    surname = tk.Label(root, text="Surname:", font=("Helvetica", 16), bg="white")
    surname.place(x=20, y=11)

    age = tk.Label(root, text="Age:", font=("Helvetica", 16), bg="white")
    age.place(x=20, y=11)

    jobtitel = tk.Label(root, text="Job Titel", font=("Helvetica", 16), bg="white")
    jobtitel.place(x=20, y=11)

    email = tk.Label(root, text="Age", font=("Helvetica", 16), bg="white")
    email.place(x=20, y=11)

    telephone = tk.Label(root, text="Telephone", font=("Helvetica", 16), bg="white")
    telephone.place(x=20, y=11)

    country = tk.Label(root, text="Country", font=("Helvetica", 16), bg="white")
    country.place(x=20, y=11)

    address = tk.Label(root, text="Address", font=("Helvetica", 16), bg="white")
    address.place(x=20, y=11)

    join = tk.Label(root, text="Age", font=("Helvetica", 16), bg="white")
    age.place(x=20, y=11)