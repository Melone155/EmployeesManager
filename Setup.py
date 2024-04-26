import tkinter as tk
from PIL import Image, ImageTk
import os
import customtkinter
import YML

class Click:
    pass

def Setupstart(root):
    Employees = 'Config/Employees.yaml'

    if not os.path.exists(Employees):
        # Bild laden und konvertieren
        image = Image.open("Picture/Logo.png")
        image = image.resize((460, 327))  # Größe anpassen
        tk_image = ImageTk.PhotoImage(image)

        # Label für das Bild erstellen und hinzufügen
        label = tk.Label(root, image=tk_image)
        label.image = tk_image  # Referenz behalten, um das Bild vor dem Garbage Collection zu behalten
        label.pack(pady=20)

        main_font = customtkinter.CTkFont(family="Helvetica", size=12)

        Setup_Wizard_Button = customtkinter.CTkButton(
            master=root,
            command=button_click,
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

def button_click():
    print("Test wurde geklickt")