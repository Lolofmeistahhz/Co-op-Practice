from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import *
from tkinter import  END, Text
global default_font_size
default_font_size = 12
default_font_family = "Consolas"

def open_file(textbox: Text): # textbox это textbox
    filepath = askopenfilename()
    with open(filepath, "r") as file:
        content = file.read()
    textbox.delete("1.0", END) # 1.0 line.column
    textbox.insert("1.0", content)
def save_file(textbox: Text):
    path = asksaveasfilename(filetypes=[('ALL Files', '*')])
    with open(path, "w") as file:
        file.write(textbox.get("1.0", END))
def add_font_size(textbox: Text()):
    default_font_size = default_font_size + 2
    textbox.config(font=(default_font_family, default_font_size))
def minus_font_size(textbox: Text()):
    default_font_size = default_font_size - 2
    textbox.config(font=(default_font_family, default_font_size))