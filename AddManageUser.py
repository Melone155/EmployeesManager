import os
import tkinter as tk
from tkinter import *

import customtkinter
import yaml
from customtkinter.windows.widgets import ctk_button

import EmployeeManager


def AddEmployee(root):
    for widget in root.winfo_children():
        widget.destroy()

    # Navbar
    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=20, y=11)

    back.bind("<Button-1>", lambda event: EmployeeManager.NormalScreen(root))