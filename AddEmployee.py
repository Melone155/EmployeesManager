import os
import tkinter as tk
from tkinter import *

import customtkinter
import yaml
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
        command= lambda: Save(root),
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


def Save(root):
    global form_entries
    data = {}

    for field in fields:
        entry = form_entries[field]
        value = entry.get()
        if not value:
            user = tk.Label(root, text="Something is not correct or something is missing please check your input" ,fg="red", font=("Helvetica", 16), bg="white")
            user.place(x=100, y=451)

            entry.config(fg="red")
            return
        data[field] = value

        if field == "Telephone" and not value.isdigit():
            entry.config(fg="red")
            return
        if field == "Email" and not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            entry.config(fg="red")
            return
        if field in ["Joining the company", "Pension start date"]:
            try:
                datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                entry.config(fg="red")
                return
        if field == "Pay":
            try:
                float(value)
            except ValueError:
                entry.config(fg="red")
                return

    save_yml(data)

    save_yml(data)
    print("Save")


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

def save_yml(data):
    file_path = "Config/Employees.yaml"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = yaml.safe_load(file) or {}
    else:
        existing_data = {}

    if 'Employees' not in existing_data:
        existing_data['Employees'] = {}

    next_id = len(existing_data['Employees']) + 1
    existing_data['Employees'][next_id] = data

    with open(file_path, 'w') as file:
        yaml.dump(existing_data, file, default_flow_style=False)