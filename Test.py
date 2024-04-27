import tkinter as tk
from PIL import Image, ImageTk
import os
import customtkinter
import Setup

continueWizard = 0

def Setupstart(root):
    MySQL = 'Config/MySQL.yaml'
    Employees = 'Config/Employees.yaml'
    User = 'Config/User.yaml'

    if not os.path.exists(Employees) or not os.path.exists(MySQL) or not os.path.exists(User):

        image = Image.open("Picture/Logo.png")
        image = image.resize((460, 327))  # Größe anpassen
        tk_image = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=tk_image)
        label.image = tk_image
        label.pack(pady=20)

        main_font = customtkinter.CTkFont(family="Helvetica", size=12)

        Setup_Wizard_Button = customtkinter.CTkButton(
            master=root,
            command=start_Wizard(),  # Hier wird eine Lambda-Funktion verwendet, um die Funktion start_Wizard aufzurufen
            text="Setup Wizard",
            font=main_font,
            text_color="black",
            height=40,
            width=120,
            border_width=2,
            corner_radius=3,
            border_color="#d3d3d3",
            bg_color="#ffffff",
            fg_color="#ffffff",
            hover=False
        )

        Setup_Wizard_Button.place(x=400, y=400)

def start_Wizard():
    global continueWizard
    continueWizard += 1
    print("Setup-Assistent wird gestartet...")
    # Hier den Code für den Setup-Assistenten einfügen

# Hauptfenster erstellen
root = tk.Tk()
root.title("Mitarbeiter Management Programm")
root.geometry("900x600")

# Setup Wizard starten
Setup.Setupstart(root)

# GUI-Schleife starten
root.mainloop()
