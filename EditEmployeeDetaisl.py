import os
import tkinter as tk
from tkinter import Frame, Label, Entry
import yaml

import EmployeeDetails

fields = ["Last Name", "First Name", "Job", "Country", "Address", "Telephone", "Email", "Position", "Joining the company", "Pay", "Pension start date", "Age"]


def Edit(root, emp_id):
    for widget in root.winfo_children():
        widget.destroy()

    initial_values = load_data(emp_id)

    # Navbar
    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=50, y=11)

    save_button = tk.Label(root, text="Save", font=("Helvetica", 16), bg="white")
    save_button.place(x=830, y=11)

    form_entries = makeform(root, fields, initial_values)

    save_button.bind("<Button-1>", lambda event: save_data(emp_id, form_entries, root))

    back.bind("<Button-1>", lambda event: EmployeeDetails.Details(root, emp_id))


def makeform(root, fields, initial_values=None):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, text=field, width=17, font=("Helvetica", 12), anchor='w')
        ent = Entry(row, width=30, font=("Helvetica", 12))
        if initial_values and field in initial_values:
            ent.insert(0, initial_values[field])  # Setze den Anfangswert
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, fill=tk.X)
        entries[field] = ent
    return entries


def load_data(emp_id):
    file_path = "Config/Employees.yaml"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file) or {}
        return data.get('Employees', {}).get(emp_id, {})
    return {}


def save_data(emp_id, entries, root):
    file_path = "Config/Employees.yaml"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = yaml.safe_load(file) or {}
    else:
        existing_data = {'Employees': {}}

    data = {}
    for field in fields:
        data[field] = entries[field].get()

    existing_data['Employees'][emp_id] = data

    with open(file_path, 'w') as file:
        yaml.dump(existing_data, file, default_flow_style=False)

    EmployeeDetails.Details(root, emp_id)
