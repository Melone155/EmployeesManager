import tkinter as tk
from tkinter import *
import re
from datetime import datetime
import yaml
import os
import customtkinter
from customtkinter.windows.widgets import ctk_button
import EmployeeManager

fields = "Last Name", "First Name", "Job", "Country", "Address", "Telephone", "Email", "Position", "Joining the company", "Pay", "Pension start date"

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def is_valid_date(date_string, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def write_to_yaml(file_path, data):
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
    form_entries = makeform(root, fields)

    # Save Button
    main_font = customtkinter.CTkFont(family="Helvetica", size=12)
    Save_Button = ctk_button.CTkButton(
        master=root,
        text="Save",
        command=lambda: validate_and_save(form_entries),
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

def validate_and_save(entries):
    valid = True
    data = {}
    for field, entry in entries.items():
        value = entry.get()
        if field == "Email" and not is_valid_email(value):
            entry.config(fg="red")
            valid = False
        elif field == "Pension start date" and not is_valid_date(value):
            entry.config(fg="red")
            valid = False
        elif field == "Telephone":
            try:
                float(value)
                entry.config(fg="black")
            except ValueError:
                entry.config(fg="red")
                valid = False
        else:
            entry.config(fg="black")
        data[field] = value

    if valid:
        write_to_yaml("employee_data.yaml", data)
        print("Daten erfolgreich gespeichert.")
    else:
        print("Fehlerhafte Eingaben. Bitte kor")
