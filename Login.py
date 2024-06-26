import tkinter as tk
import yaml
from PIL import Image, ImageTk
import customtkinter
from customtkinter.windows.widgets import ctk_button

import EmployeeManager
import config

def LoginScreen(root):
    # Clear All Old Objects
    for widget in root.winfo_children():
        widget.destroy()

    image = Image.open("Picture/Logo.png")
    image = image.resize((306, 218))  # Größe anpassen
    tk_image = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=tk_image)
    label.image = tk_image
    label.pack(pady=20)

    Userlabe = tk.Label(root, text="Username", font=("Helvetica", 16))
    Userlabe.place(x=336, y=284)

    Userentry = tk.Entry(root)
    Userentry.place(x=440, y=290)

    passwordlabe = tk.Label(root, text="Password", font=("Helvetica", 16))
    passwordlabe.place(x=336, y=319)

    passwordentry = tk.Entry(root, show="*")
    passwordentry.place(x=440, y=325)

    main_font = customtkinter.CTkFont(family="Helvetica", size=12)

    Setup_Wizard_Button = ctk_button.CTkButton(
        master=root,
        text="Login",
        font=main_font,
        text_color="black",
        height=40,
        width=120,
        border_width=2,
        corner_radius=3,
        border_color="#d3d3d3",
        bg_color="#ffffff",
        fg_color="#ffffff",
        hover=False,
        command=lambda: Login(Userentry.get(), passwordentry.get(), root)
    )

    Setup_Wizard_Button.place(x=387, y=360)

def Login(User, Password, root):
    if UserRequest(User, Password):
        # User login was successful
        config.loginuser = User
        config.permission = get_permission(User)
        EmployeeManager.NormalScreen(root)
    else:
        labe = tk.Label(root, text="The username or password is incorrect. Try again", font=("Helvetica", 13))
        labe.place(x=270, y=410)

def UserRequest(username, password):
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
            if user_info.get('Passwort') == password:
                return True
    return False

def get_permission(user):
    try:
        with open('Config/User.yaml', 'r') as file:
            userdata = yaml.safe_load(file)
    except FileNotFoundError:
        print("User.yaml file not found.")
        return ""

    users = userdata.get('User', {})
    user_info_list = users.get(user)

    if user_info_list:
        for user_info in user_info_list:
            return user_info.get('permission')
    return ""