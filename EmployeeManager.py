import tkinter as tk
from PIL import Image, ImageTk

import AddEmployee
OpenMenu = True
def NormalScreen(root):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=900, height=50)
    canvas.pack()

    bg_color = "#FFFFFF"
    canvas.create_rectangle(0, 0, 1000, 50, fill=bg_color, outline="")

    add = tk.Label(root, text="Add", font=("Helvetica", 16), bg="white")
    add.place(x=840, y=11)

    options = tk.Label(root, text="Settings", font=("Helvetica", 16), bg="white")
    options.place(x=20, y=11)

    add.bind("<Button-1>", lambda event: AddEmployee.AddEmployee(root))
    options.bind("<Button-1>", lambda event: Settingsmenu(root))


def Settingsmenu(root):
    global OpenMenu
    if OpenMenu == True:
        canvas = tk.Canvas(root, width=10000, height=10000)
        canvas.pack()

        bg_color = "#FFFFFF"
        canvas.create_rectangle(0, 0, 100, 1000, fill=bg_color, outline="")

        user = tk.Label(root, text="User", font=("Helvetica", 16), bg="white")
        user.place(x=10, y=81)

        importdata = tk.Label(root, text="Import", font=("Helvetica", 16), bg="white")
        importdata.place(x=10, y=121)

        export = tk.Label(root, text="Export", font=("Helvetica", 16), bg="white")
        export.place(x=10, y=161)

        OpenMenu = False
    else:
        for widget in root.winfo_children():
            widget.destroy()
        OpenMenu = True
        NormalScreen(root)

#def display_yaml_data(root, file_path):
#    data = load_yaml_data(file_path)#
#
#    # Erstellen des Textwidgets
#    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
#    text_area.pack(expand=True, fill="both")

    # Hinzufügen der Daten zum Textwidget
 #   text_area.insert(tk.INSERT, yaml.dump(data, default_flow_style=False))
#    text_area.configure(state='disabled')