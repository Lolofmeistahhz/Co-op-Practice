from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import *
from tkinter import  END, Text
default_font_size = 12
default_font_family = "Consolas"
is_default_theme = True
def open_file(textbox): # textbox СЌС‚Рѕ textbox
    filepath = askopenfilename()
    if filepath == '':
        return
    with open(filepath, "r") as file:
        content = file.read()
    textbox.delete("1.0", END) # 1.0 line.column
    textbox.insert("1.0", content)
def save_file(textbox):
    path = asksaveasfilename(filetypes=[('ALL Files', '*')])
    if path == '':
        return
    with open(path, "w") as file:
        file.write(textbox.get("1.0", END))

def add_font_size(textbox):
    global default_font_size
    if default_font_size > 36:
        default_font_size = default_font_size
    else:
        default_font_size = default_font_size + 2
        textbox.config(font=(default_font_family, default_font_size))
def minus_font_size(textbox):
    global default_font_size
    if default_font_size < 8:
        default_font_size = default_font_size
    else:
        default_font_size = default_font_size - 2
        textbox.config(font=(default_font_family, default_font_size))
<<<<<<< HEAD
=======

def dark_mode(textbox):
    textbox.configure(bg="#000000",fg="#FF6600")
def light_mode(textbox):
    textbox.configure(bg="#ffffff",fg="#000000")
>>>>>>> 05aa0ed1a390371cf11f5b5cb1eb73fe347d1b37

def dark_mode(textbox: Text):
    textbox.configure(bg="#000000",fg="#FF6600", insertbackground="white")
def light_mode(textbox: Text):
    textbox.configure(bg="#ffffff",fg="#000000", insertbackground="black")

def swap_theme(textbox):
    global is_default_theme
    if is_default_theme: 
        dark_mode(textbox)
    else: 
        light_mode(textbox)
    is_default_theme = not is_default_theme