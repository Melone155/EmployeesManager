import os
import time
import tkinter as tk
from tkinter import Frame, Label, Button, Entry
import yaml

import EmployeeManager
import ManageUser
import ManageUserDetails


def ChangePasswort(root, username):

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
    passwortlabel = tk.Label(root, text="Passwort", font=("Helvetica", 16))
    passwortlabel.place(x=250, y=100)

    passwortentry = tk.Entry(root, width=20, show="*")
    passwortentry.place(x=250, y=130)

    global var
    var = tk.StringVar()

    save_button.bind("<Button-1>", lambda event: SaveCreate(root, username, passwortentry.get(), var.get()))
    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))

    # Load data if username is provided
    if username:
        file_path = "Config/User.yaml"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = yaml.safe_load(file) or {}

            user_data = existing_data.get('User', {}).get(username, [{}])[0]

            username.insert(0, username)
            passwortentry.insert(0, user_data.get('Passwort', ''))
            var.set(user_data.get('permission', ''))

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

    existing_data['User'][username] = [new_user]

    with open(file_path, 'w') as file:
        yaml.dump(existing_data, file, default_flow_style=False)

    success = tk.Label(root, text="User Passwort Change", font=("Helvetica", 16), fg="green")
    success.place(x=50, y=300)

    time.sleep(2)

    EmployeeManager.NormalScreen(root)
