import os
import tkinter as tk
from tkinter import Frame, Label, Button, Entry
import yaml

import ChangePasswort
import CreateManageUser
import EmployeeManager

import os
import tkinter as tk
from tkinter import Canvas, Label
import yaml
import config

import ManageUserDetails

OpenMenu = False


def ManageUserOverview(root):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=900, height=50, bg="#FFFFFF")
    canvas.grid(row=0, column=0, columnspan=3, sticky='ew')

    add = tk.Label(root, text="Add", font=("Helvetica", 16), bg="white")
    add.grid(row=0, column=2, sticky='e', padx=20)

    options = tk.Label(root, text="Settings", font=("Helvetica", 16), bg="white")
    options.grid(row=0, column=0, sticky='w', padx=20)

    add.bind("<Button-1>", lambda event: CreateManageUser.Create(root))
    options.bind("<Button-1>", lambda event: Settingsmenu(root))

    data = load_user_data()
    display_data(root, data)


def Settingsmenu(root):
    global OpenMenu
    if OpenMenu:
        settings_frame = Frame(root, bg="#FFFFFF")
        settings_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

        user = tk.Label(settings_frame, text="Employees", font=("Helvetica", 16), bg="white")
        user.grid(row=0, column=0, sticky='w', padx=10, pady=5)

        passwort = tk.Label(settings_frame, text="Passwort", font=("Helvetica", 16), bg="white")
        passwort.grid(row=1, column=0, sticky='w', padx=10, pady=5)

        user.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))

        passwort.bind("<Button-1>", lambda event: ChangePasswort.Change(root, config.loginuser))

        OpenMenu = False
    else:
        for widget in root.winfo_children():
            widget.destroy()
        OpenMenu = True
        ManageUserOverview(root)


def load_user_data():
    file_path = "Config/User.yaml"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file) or {}
        return data.get('User', {})
    return {}

def display_data(root, data):
    # Nur den Datenanzeigebereich löschen
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
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
        for username, details in data.items():
            frame = Frame(main_frame, borderwidth=1, relief="solid", pady=5, padx=5)
            frame.grid(row=row, column=0, padx=0, pady=0, sticky='ew')

            name_label = Label(frame, text=username, font=("Helvetica", 16))
            name_label.pack(side="left", padx=5, pady=5)

            view_button = Button(frame, text=">", font=("Helvetica", 16), command=lambda: ManageUserDetails.show_user_details(root, username, details))
            view_button.pack(side="right", padx=5, pady=5)

            row += 1

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)