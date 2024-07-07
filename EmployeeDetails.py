import os
import tkinter as tk
from tkinter import *

import customtkinter
import yaml
from customtkinter.windows.widgets import ctk_button

import EditEmployeeDetaisl
import EmployeeManager


def Details(root, id):
    for widget in root.winfo_children():
        widget.destroy()

    # Navbar
    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=50, y=11)

    edit = tk.Label(root, text="Edit", font=("Helvetica", 16), bg="white")
    edit.place(x=830, y=11)

    delete = tk.Label(root, text="Delete", font=("Helvetica", 16), bg="white")
    delete.place(x=750, y=11)

    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))
    edit.bind("<Button-1>", lambda event: EditEmployeeDetaisl.Edit(root, id))
    delete.bind("<Button-1>", lambda event: delete_employee_entry("Config/Employees.yaml", id, root))

    strem = open("Config/Employees.yaml")
    dictionary = yaml.safe_load(strem)

    #First Name
    name = tk.Label(root, text="Name:", font=("Helvetica", 16))
    name.place(x=50, y=60)

    namefill = tk.Label(root, text=dictionary["Employees"][id]["First Name"], font=("Helvetica", 16))
    namefill.place(x=60, y=90)

    #Last Name
    surname = tk.Label(root, text="Surname:", font=("Helvetica", 16))
    surname.place(x=210, y=62)

    surnamefill = tk.Label(root, text=dictionary["Employees"][id]["Last Name"], font=("Helvetica", 16))
    surnamefill.place(x=220, y=90)

    #Age
    agelabel = tk.Label(root, text="Age:", font=("Helvetica", 16))
    agelabel.place(x=350, y=62)

    agefill = tk.Label(root, text=dictionary["Employees"][id]["Age"], font=("Helvetica", 16))
    agefill.place(x=360, y=90)

    jobtitel = tk.Label(root, text="Job Titel:", font=("Helvetica", 16))
    jobtitel.place(x=440, y=62)

    jobtitelfill = tk.Label(root, text=dictionary["Employees"][id]["Position"], font=("Helvetica", 16))
    jobtitelfill.place(x=450, y=90)

    country = tk.Label(root, text="Country", font=("Helvetica", 16))
    country.place(x=600, y=62)

    countryfill = tk.Label(root, text=dictionary["Employees"][id]["Country"], font=("Helvetica", 16))
    countryfill.place(x=610, y=90)

    email = tk.Label(root, text="Email:", font=("Helvetica", 16))
    email.place(x=50, y=152)

    mailfill = tk.Label(root, text=dictionary["Employees"][id]["Email"], font=("Helvetica", 16))
    mailfill.place(x=60, y=178)

    telephone = tk.Label(root, text="Telephone", font=("Helvetica", 16))
    telephone.place(x=400, y=152)

    telephonefill = tk.Label(root, text=dictionary["Employees"][id]["Telephone"], font=("Helvetica", 16))
    telephonefill.place(x=410, y=178)

    Job = tk.Label(root, text="Job", font=("Helvetica", 16))
    Job.place(x=640, y=152)

    Jobfill = tk.Label(root, text=dictionary["Employees"][id]["Job"], font=("Helvetica", 16))
    Jobfill.place(x=650, y=178)

    JoinCompany = tk.Label(root, text="Joining the Company", font=("Helvetica", 16))
    JoinCompany.place(x=50, y=220)

    JoinFill = tk.Label(root, text=dictionary["Employees"][id]["Joining the company"], font=("Helvetica", 16))
    JoinFill.place(x=60, y=250)

    LeaveCompany = tk.Label(root, text="Pension start date", font=("Helvetica", 16))
    LeaveCompany.place(x=280, y=220)

    LeaveFill = tk.Label(root, text=dictionary["Employees"][id]["Pension start date"], font=("Helvetica", 16))
    LeaveFill.place(x=290, y=250)

    Pay = tk.Label(root, text="Pay", font=("Helvetica", 16))
    Pay.place(x=490, y=220)

    PayFill = tk.Label(root, text=dictionary["Employees"][id]["Pay"], font=("Helvetica", 16))
    PayFill.place(x=500, y=250)

    Adress = tk.Label(root, text="Address:", font=("Helvetica", 16))
    Adress.place(x=600, y=220)

    PayFill = tk.Label(root, text=dictionary["Employees"][id]["Address"], font=("Helvetica", 16))
    PayFill.place(x=610, y=250)

def delete_employee_entry(file_path, employee_id, root):
    # Datei einlesen
    with open(file_path, 'r') as file:
        employees_data = yaml.safe_load(file)

    # Eintrag löschen, falls vorhanden
    if employee_id in employees_data['Employees']:
        del employees_data['Employees'][employee_id]
        EmployeeManager.NormalScreen(root)

    # Datei erneut speichern
    with open(file_path, 'w') as file:
        yaml.safe_dump(employees_data, file, default_flow_style=False)