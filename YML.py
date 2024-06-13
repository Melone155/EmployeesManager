import os
import tkinter as tk
from tkinter import Frame, Label, Entry, TOP, X, LEFT
import re
from datetime import datetime
import yaml

fields = ["Last Name", "First Name", "Job", "Country", "Address", "Telephone", "Email", "Position", "Joining the company", "Pay", "Pension start date"]

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

    form_entries = makeform(root, fields)

    Save_Button = tk.Button(
        root,
        text="Save",
        command=lambda: validate_and_save(form_entries)
    )
    Save_Button.pack()

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
            if not value.isdigit():
                entry.config(fg="red")
                valid = False
            else:
                entry.config(fg="black")
        else:
            entry.config(fg="black")
        data[field] = value

    if valid:
        write_to_yaml("employee_data.yaml", data)
        print("Daten erfolgreich gespeichert.")
    else:
        print("Fehlerhafte Eingaben. Bitte korrigieren Sie die markierten Felder.")

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, text=field, width=20, anchor='w')
        ent = Entry(row, width=30)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=X)
        entries[field] = ent
    return entries

def CreateConfigs(status, database, host, password, user):
    mysql_config = {
        'MySQL': [{
            'Database': database,
            'Host': host,
            'Password': password,
            'Status': status,
            'User': user
        }]
    }

    employees = {}

    user = {
        'User': {
            'Admin': [{
                'Passwort': 'admin',
                'permission': '*'
            }]
        }
    }

    mysql_path = "Config/MySQL.yaml"
    os.makedirs(os.path.dirname(mysql_path), exist_ok=True)

    employees_path = "Config/Employees.yaml"
    os.makedirs(os.path.dirname(employees_path), exist_ok=True)

    user_path = "Config/User.yaml"
    os.makedirs(os.path.dirname(user_path), exist_ok=True)

    with open(mysql_path, 'w') as file:
        yaml.dump(mysql_config, file, default_flow_style=False)

    with open(employees_path, 'w') as file:
        yaml.dump(employees, file, default_flow_style=False)

    with open(user_path, 'w') as file:
        yaml.dump(user, file, default_flow_style=False)
