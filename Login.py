import tkinter as tk

import yaml
from PIL import Image, ImageTk
import customtkinter
from customtkinter.windows.widgets import ctk_button

import EmployeeManager

IsLogin = False

def LoginScreen(root):

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
        text="Finished",
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
        command=
        lambda: Login(Userentry.get(), passwordentry.get(), root)
    )

    Setup_Wizard_Button.place(x=387, y=360)


def Login(User, Password, root):
    if UserRequest(User, Password):
       #User login was successful
        EmployeeManager.NormalScreen(root)
    else:
        labe = tk.Label(root, text="The username or password is incorrect try again", font=("Helvetica", 13))
        labe.place(x=270, y=410)

def UserRequest(username, password):
    try:
        with open('Config/User.yaml', 'r') as file:
            userdata = yaml.safe_load(file)
    except FileNotFoundError:
        print("User.yaml file not found.")
        return False

    users = userdata.get('User', {})
    user_info = users.get(username)

    if user_info and user_info.get('Passwort') == password:
        return True
    return False
