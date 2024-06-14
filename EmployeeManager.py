import os
import tkinter as tk
from tkinter import Frame, Label, Button, Entry
import yaml

import AddEmployee
import ChangePasswort
import EmployeeDetails
import ManageUser
#from Login import loginuser

OpenMenu = True


def NormalScreen(root):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=900, height=50, bg="#FFFFFF")
    canvas.grid(row=0, column=0, columnspan=2, sticky='ew')

    add = tk.Label(root, text="Add", font=("Helvetica", 16), bg="white")
    add.grid(row=0, column=1, sticky='e', padx=20)

    options = tk.Label(root, text="Settings", font=("Helvetica", 16), bg="white")
    options.grid(row=0, column=0, sticky='w', padx=20)

    add.bind("<Button-1>", lambda event: AddEmployee.AddEmployee(root))
    options.bind("<Button-1>", lambda event: Settingsmenu(root))

    search_entry = Entry(root, font=("Helvetica", 14))
    search_entry.grid(sticky='w', padx=7, pady=10)

    search_button = Button(root, text="Search", font=("Helvetica", 14), command=lambda: search_data(root, search_entry.get()))
    search_button.grid(row=1,)

    data = load_data()
    display_data(root, data)


def Settingsmenu(root):
    global OpenMenu
    if OpenMenu:
        settings_frame = Frame(root, bg="#FFFFFF")
        settings_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

        user = tk.Label(settings_frame, text="User", font=("Helvetica", 16), bg="white")
        user.grid(row=0, column=0, sticky='w', padx=10, pady=5)

        passwort = tk.Label(settings_frame, text="Passwort", font=("Helvetica", 16), bg="white")
        passwort.grid(row=1, column=0, sticky='w', padx=10, pady=5)

        user.bind("<Button-1>", lambda event: ManageUser.ManageUserOverview(root))

        #passwort.bind("<Button-1>", lambda event: ChangePasswort.ChangePasswort(root, loginuser))

        OpenMenu = False
    else:
        for widget in root.winfo_children():
            widget.destroy()
        OpenMenu = True
        NormalScreen(root)


def load_data():
    file_path = "Config/Employees.yaml"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file) or {}
        return data.get('Employees', {})
    return {}


def display_data(root, data):
    # Nur den Datenanzeigebereich löschen
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:  # Behalte die ersten beiden Zeilen (Navbar und Suchleiste)
            widget.grid_forget()

    container = Frame(root)
    container.grid(row=2, column=0, columnspan=3, padx=3, pady=3, sticky='nsew')

    main_frame = Frame(container)
    main_frame.pack(padx=0, pady=0, expand=True, fill='both')

    if not data:
        no_data_label = Label(main_frame, text="No employees data found.", font=("Helvetica", 16))
        no_data_label.pack(padx=0, pady=0)
    else:
        row = 0
        for emp_id, details in data.items():
            frame = Frame(main_frame, borderwidth=1, relief="solid", pady=5, padx=5)
            frame.grid(row=row, column=0, padx=0, pady=0, sticky='ew')

            name = f"{details['Last Name']}, {details['First Name']}"
            name_label = Label(frame, text=name, font=("Helvetica", 16))
            name_label.pack(side="left", padx=5, pady=5)

            view_button = Button(frame, text=">", font=("Helvetica", 16),
                                 command=lambda: EmployeeDetails.Details(root, emp_id))
            view_button.pack(side="right", padx=5, pady=5)

            row += 1

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)


def search_data(root, query):
    data = load_data()
    if query:
        filtered_data = {k: v for k, v in data.items() if
                         query.lower() in (v['First Name'].lower() + ' ' + v['Last Name'].lower())}
    else:
        filtered_data = data
    display_data(root, filtered_data)
