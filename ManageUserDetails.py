import os
import tkinter as tk
from tkinter import Frame, Label, Button, Entry
import yaml

import EditManageUser
import EmployeeManager

import os
import tkinter as tk
from tkinter import Canvas, Label
import yaml

import ManageUser


def show_user_details(root, username, details):

    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    back = tk.Label(root, text="Back", font=("Helvetica", 16), bg="white")
    back.place(x=50, y=11)

    edit_button = tk.Label(root, text="Edit", font=("Helvetica", 16), bg="white")
    edit_button.place(x=830, y=11)

    edit_button.bind("<Button-1>", lambda event: EditManageUser.Edit(root, username, details))
    back.bind("<Button-1>", lambda event: ManageUser.ManageUserOverview(root))

    for detail in details:

        userlabel = tk.Label(root, text="User: " + username, font=("Helvetica", 16))
        userlabel.place(x=50, y=100)

        permissionlabel = tk.Label(root, text="Permission: " + detail.get('permission'), font=("Helvetica", 16))
        permissionlabel.place(x=50, y=140)