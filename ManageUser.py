import os
import tkinter as tk
from tkinter import Frame, Label, Button
import yaml

import EmployeeManager

import os
import tkinter as tk
from tkinter import Canvas, Label
import yaml

def ManageUserOverview(root):

    for widget in root.winfo_children():
        widget.destroy()

    # Navbar
    canvas = Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=50, y=11)

    create_button = Label(root, text="Create", font=("Helvetica", 16), bg="white")
    create_button.place(x=800, y=11)

    create_button.bind("<Button-1>", lambda event: Create(root))
    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))

    #Data Grid
    data = load_data()
    display_data(root, data)

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
        if int(widget.grid_info()["row"]) > 0:  # Behalte die erste Zeile (Navbar)
            widget.grid_forget()


    container = Frame(root)
    container.grid(row=1, column=0, columnspan=2, padx=3, pady=3, sticky='nsew')

    main_frame = Frame(container)
    main_frame.pack(padx=0, pady=0, expand=True, fill='both')

    if not data:
        no_data_label = Label(main_frame, text="No employees datas found.", font=("Helvetica", 16))
        no_data_label.pack(padx=0, pady=0)
    else:
        row = 0
        for emp_id, details in data.items():
            frame = Frame(main_frame, borderwidth=1, relief="solid", pady=5, padx=5)
            frame.grid(row=row, column=0, padx=0, pady=0, sticky='ew')

            name = f"{details['Last Name']}"
            name_label = Label(frame, text=name, font=("Helvetica", 16))
            name_label.pack(side="left", padx=5, pady=5)

            view_button = Button(frame, text=">", font=("Helvetica", 16), command=lambda: print("SOON"))
            view_button.pack(side="right", padx=5, pady=5)

            row += 1

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

def Create(root):
    for widget in root.winfo_children():
        widget.destroy()

    # Navbar
    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=50, y=11)

    save_button = tk.Label(root, text="Save", font=("Helvetica", 16), bg="white")
    save_button.place(x=830, y=11)

    # Input
    namelabel = tk.Label(root, text="User Name", font=("Helvetica", 16))
    namelabel.place(x=50, y=100)

    nameentry = tk.Entry(root, width=20)
    nameentry.place(x=50, y=130)

    passwortlabel = tk.Label(root, text="Passwort", font=("Helvetica", 16))
    passwortlabel.place(x=250, y=100)

    passwortentry = tk.Entry(root, width=20, show="*")
    passwortentry.place(x=250, y=130)

    global var
    var = tk.StringVar()

    permissionlabel = tk.Label(root, text="Permissions", font=("Helvetica", 16))
    permissionlabel.place(x=50, y=175)

    admin = tk.Radiobutton(root, text="Admin", variable=var, value="*", font=("Helvetica", 16))
    admin.place(x=50, y=200)

    readwrite = tk.Radiobutton(root, text="Read and Write", variable=var, value="rw", font=("Helvetica", 16))
    readwrite.place(x=50, y=230)

    read = tk.Radiobutton(root, text="Read Only", variable=var, value="r", font=("Helvetica", 16))
    read.place(x=50, y=260)

    save_button.bind("<Button-1>", lambda event: SaveCreate(root, nameentry.get(), passwortentry.get(), var.get()))
    back.bind("<Button-1>", lambda event: ManageUserOverview(root))

def SaveCreate(root, username, password, permission):
    if not username or not password:
        error = tk.Label(root, text="Username and Password are required", font=("Helvetica", 16), fg="red")
        error.place(x=50, y=300)
        return

    file_path = "Config/User.yaml"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = yaml.safe_load(file) or {}
    else:
        existing_data = {}

    if 'User' not in existing_data:
        existing_data['User'] = {}

    new_user = {
        'Passwort': password,
        'permission': permission
    }

    existing_data['User'][username] = new_user

    with open(file_path, 'w') as file:
        yaml.dump(existing_data, file, default_flow_style=False)

    success = tk.Label(root, text="User successfully saved", font=("Helvetica", 16), fg="green")
    success.place(x=50, y=300)
