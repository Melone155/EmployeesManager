import os
import time
import tkinter as tk
from tkinter import Frame, Label, Button, Entry
import yaml

import ManageUser
import ManageUserDetails
import config  # Importiere das neue Modul

def Change(root, username):
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

    save_button.bind("<Button-1>", lambda event: Save(root, config.loginuser, passwortentry.get(), getpermission(config.loginuser)))
    back.bind("<Button-1>", lambda event: ManageUserDetails.show_user_details(root, username))

def Save(root, username, password, permission):
    if not password:
        error = tk.Label(root, text="Password are required", font=("Helvetica", 16), fg="red")
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

    success = tk.Label(root, text="New Passwort successfully saved", font=("Helvetica", 16), fg="green")
    success.place(x=50, y=300)

    time.sleep(2)

    ManageUser.ManageUserOverview(root)

def getpermission(username):
    try:
        with open('Config/User.yaml', 'r') as file:
            userdata = yaml.safe_load(file)
    except FileNotFoundError:
        print("User.yaml file not found.")
        return False

    users = userdata.get('User', {})
    user_info_list = users.get(username)

    if user_info_list:
        for user_info in user_info_list:
            return user_info.get('permission')
