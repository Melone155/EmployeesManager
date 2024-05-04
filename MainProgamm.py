import tkinter as tk
import os

import Login
import Setup

# Hauptfenster erstellen
root = tk.Tk()
root.title("Employee Management Programme")
root.geometry("900x600")

# Setup Wizard starten
Setup.Setupstart(root)

# GUI-Schleife starten
root.mainloop()