import tkinter as tk
from PIL import Image, ImageTk
import customtkinter
import os

import Setup

# Create main window
root = tk.Tk()
root.title("Mitarbeiter Management Programm")
root.geometry("900x600")

# Setup Wizzard
Setup.Setupstart(root)


root.mainloop()
