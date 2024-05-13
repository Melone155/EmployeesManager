import tkinter as tk
from tkinter import *

import customtkinter
from customtkinter.windows.widgets import ctk_button

import re

from datetime import datetime

import EmployeeManager

fields = "Last Name", "First Name", "Job", "Country", "Address", "Telephone", "Email", "Position", "Joining the company", "Pay", "Pension start date"


def AddEmployee(root):
    for widget in root.winfo_children():
        widget.destroy()

    # Navbar

    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=20, y=11)

    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))

    # Formular
    global form_entries
    form_entries = makeform(root, fields)

    # Save Button
    main_font = customtkinter.CTkFont(family="Helvetica", size=12)
    Save_Button = ctk_button.CTkButton(
        master=root,
        text="Save",
        command= lambda: Save(),
        font=main_font,
        text_color="black",
        height=40,
        width=120,
        border_width=2,
        corner_radius=3,
        border_color="#d3d3d3",
        bg_color="#ffffff",
        fg_color="#ffffff",
        hover=False
    )

    Save_Button.place(x=400, y=500)


def Save():
    telephone_entry = form_entries["Telephone"]
    telephone = telephone_entry.get()

    Email_entry = form_entries["Email"]
    Email = telephone_entry.get()

    Join_entry = form_entries["Joining the company"]
    Join = telephone_entry.get()

    Pension_entry = form_entries["Joining the company"]
    Pension = telephone_entry.get()

    pay_entry = form_entries["Pay"]
    pay = telephone_entry.get()


    #Is this a Telephone Nummber
    try:
        int(telephone)
        # this Value is a nummber
    except ValueError:
        # This Value is not a Nummber
        telephone_entry.config(fg="red")

    # Is Money a integer
    try:
        float(pay)
        # this Value is a nummber
    except ValueError:
        # This Value is not a Nummber
        pay_entry.config(fg="red")

    #This is a Complete mail
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, Email):
        return True
    else:
        Email_entry.config(fg="red")

    #Is this a Date (Join)
    try:
        datetime.strptime(Join, "%d.%m.%Y")
        return True
    except ValueError:
        Join_entry.config(fg="red")

    # Is this a Date (Pension)
    try:
        datetime.strptime(Pension, "%d.%m.%Y")
        return True
    except ValueError:
        Pension_entry.config(fg="red")


def makeform(root, fields):
    entries = {}
    global ent
    for field in fields:
        row = Frame(root)
        lab = Label(row, text=field, width=17, font=("Helvetica", 12), anchor='w')
        ent = Entry(row, width=30, font=("Helvetica", 12))
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=X)
        entries[field] = ent
    return entries