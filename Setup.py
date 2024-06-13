import tkinter as tk

import mysql.connector
from PIL import Image, ImageTk
import customtkinter
from customtkinter.windows.widgets import ctk_button
import os

import Login
import EmployeeManager
import YML

var = None

def Setupstart(root):
    MySQL = 'Config/MySQL.yaml'
    Employees = 'Config/Employees.yaml'
    User = 'Config/User.yaml'

    global var
    var = tk.StringVar()

    if not os.path.exists(Employees) or not os.path.exists(MySQL) or not os.path.exists(User):

        image = Image.open("Picture/Logo.png")
        image = image.resize((460, 327))  # Größe anpassen
        tk_image = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=tk_image)
        label.image = tk_image
        label.pack(pady=20)

        main_font = customtkinter.CTkFont(family="Helvetica", size=12)

        Setup_Wizard_Button = ctk_button.CTkButton(
            master=root,
            text="Setup Wizard",
            command=lambda: start_Wizard(root),
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
    else:
        if Login.IsLogin == False:
            Login.LoginScreen(root)
            #EmployeeManager.NormalScreen(root)

def start_Wizard(root):

    image = Image.open("Picture/Logo.png")
    image = image.resize((460, 327))
    tk_image = ImageTk.PhotoImage(image)

    #Clear All Old Objects
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, image=tk_image)
    label.image = tk_image
    label.pack(pady=20)

    headline = tk.Label(root, text="Which setup do you want to use", font=("Helvetica", 16))
    headline.place(x=300, y=375)

    YML = tk.Radiobutton(root, text="YML", variable=var, value="YML")
    YML.place(x=420, y=420)

    mysql = tk.Radiobutton(root, text="MySQL", variable=var, value="MySQL")
    #mysql.place(x=420, y=443)

    main_font = customtkinter.CTkFont(family="Helvetica", size=12)

    Setup_Wizard_Button = ctk_button.CTkButton(
        master=root,
        text="Next",
        command=lambda: Finishsetup(root),
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

    Setup_Wizard_Button.place(x=397, y=480)

def Finishsetup(root):
    if var.get() == "MySQL":

        for widget in root.winfo_children():
            widget.destroy()

        image = Image.open("Picture/Logo.png")
        image = image.resize((460, 327))
        tk_image = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=tk_image)
        label.image = tk_image
        label.pack(pady=20)


        # Host
        hostlabe = tk.Label(root, text="Host", font=("Helvetica", 16))
        hostlabe.place(x=340, y=375)

        hostentry = tk.Entry(root)
        hostentry.place(x=393, y=382)

        # User
        userlabe = tk.Label(root, text="Username", font=("Helvetica", 16))
        userlabe.place(x=290, y=410)

        unserentry = tk.Entry(root)
        unserentry.place(x=393, y=417)

        # Passwort
        passwordlabel = tk.Label(root, text="Passwort", font=("Helvetica", 16))
        passwordlabel.place(x=290, y=445)

        passwordentry = tk.Entry(root, show="*")
        passwordentry.place(x=393, y=452)

        # Database
        dblabel = tk.Label(root, text="Database", font=("Helvetica", 16))
        dblabel.place(x=290, y=480)

        dbentry = tk.Entry(root, show="*")
        dbentry.place(x=393, y=487)

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
            command =
                lambda: check_mysql(hostentry.get(), unserentry.get(), passwordentry.get(), dbentry.get(), root)
        )

        Setup_Wizard_Button.place(x=397, y=530)

    else:
        YML.CreateConfigs(False, "", "", "", "")
        Login.LoginScreen(root)

def check_mysql(host, username, password, database, root):
    try:
        # Verbindung zur MySQL-Datenbank herstellen
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        # Verbindung erfolgreich hergestellt
        YML.CreateConfigs(True, host, username, password, database)

        cursor = connection.cursor()
        create_table_query = "CREATE TABLE IF NOT EXISTS Employees (First name VARCHAR(100), Surname VARCHAR(100), Place VARCHAR(100), Cost centre INT(100) Telephone number INT(100))"
        cursor.execute(create_table_query)
        cursor.close()

        connection.close()

    except mysql.connector.Error as error:
        # Verbindung konnte nicht hergestellt werden
        errorlabel = tk.Label(root, text="Database information incorrect please check your input", font=("Helvetica", 10))
        errorlabel.place(x=290, y=573)
        print(error)
