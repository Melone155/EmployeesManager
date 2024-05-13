import tkinter as tk
from tkinter import *

import customtkinter
from customtkinter.windows.widgets import ctk_button

import EmployeeManager

fields = "Last Name", "First Name", "Job", "Country", "Address", "Telephone", "Email", "Position", "Joining the company", "Pay", "Pension start date"


def AddEmployee(root):
    for widget in root.winfo_children():
        widget.destroy()

    #Navbar

    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=20, y=11)

    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))

    #Formular
    form_entries = makeform(root, fields)

    #Save Button
    main_font = customtkinter.CTkFont(family="Helvetica", size=12)
    Save_Button = ctk_button.CTkButton(
        master=root,
        text="Save",
        command=lambda: lambda event, entry=ent: get_input(event, entry),
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

    Save_Button.place(x=400, y=500)


def get_input(entries, entry):
    LastName = entries["Last Name"].get()
    FirstName = entries["First Name"].get()
    Job = entries["Job"].get()
    Country = entries["Country"].get()
    Address = entries["Address"].get()
    Telephone = entries["Telephone"].get()
    Email = entries["Email"].get()
    Joining = entries["Joining the company"].get()
    Pay = entries["Pay"].get()
    Pension = entries["Pension start date"].get()

    try:
        float(Telephone)
       #This Value is a Nummber
        print("zahl")
    except ValueError:
        #This Value is nit a Nummber
        text = entry.get()
        entry.config(fg="red")
        print("test")


def makeform(root, fields):
    entries = {}
    global ent
    for field in fields:
        row = Frame(root)
        lab = Label(row, text=field, width=17, font=("Helvetica", 12), anchor='w')
        ent = Entry(row, width=30, font=("Helvetica", 12))
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, fill=X)
        entries[field] = ent
    return entries