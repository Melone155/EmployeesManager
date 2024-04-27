import tkinter as tk

import yaml
from PIL import Image, ImageTk
import customtkinter
from customtkinter.windows.widgets import ctk_button

IsLogin = False

def LoginScreen(root):

    image = Image.open("Picture/Logo.png")
    image = image.resize((306, 218))  # Größe anpassen
    tk_image = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=tk_image)
    label.image = tk_image
    label.pack(pady=20)

    # User
    Userlabe = tk.Label(root, text="Host", font=("Helvetica", 16))
    Userlabe.place(x=340, y=375)

    Userentry = tk.Entry(root)
    Userentry.place(x=393, y=382)

    # Password
    passwordlabe = tk.Label(root, text="Password", font=("Helvetica", 16))
    passwordlabe.place(x=290, y=410)

    passwordentry = tk.Entry(root, show="*")
    passwordentry.place(x=393, y=417)

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
        lambda: Login(Userentry.get(), passwordentry.get())
    )

    Setup_Wizard_Button.place(x=397, y=530)


def Login(User, Password):
    if UserRequest(User, Password):
        print("Admin credentials are correct.")
    else:
        print("Admin credentials are incorrect.")

def UserRequest(User, Password):
    # Laden der YAML-Datei
    with open('Config/User.yaml', 'r') as file:
        userdata = yaml.safe_load(file)

    # Überprüfen, ob der Benutzer "Admin" vorhanden ist und das Passwort "admin" hat
    for user in userdata.get('User', []):
        if user.get(User) == Password:
            return True
    return False
