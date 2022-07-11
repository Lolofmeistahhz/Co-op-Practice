from tkinter import Tk, Text, Menu

from config import dark_mode, light_mode, open_file, save_file, add_font_size, minus_font_size, swap_theme
from syntax import *
window = Tk()

if __name__ == "__main__":
    window.title('Блокнот')
    window.geometry("600x400")
    window.iconbitmap("favicon.ico")
    # внешний вид
    textbox = Text(master=window, yscrollcommand=True, font=('Consolas',12))
    textbox.pack(expand=True, fill="both")
    textbox.bind("<Key>", lambda e: syntax(textbox))
    syntax_configure(textbox)
    menu = Menu(window)
    file_menu = Menu(master=menu, tearoff=False)
    file_menu.add_command(label='Открыть файл...', command=lambda: open_file(textbox))
    file_menu.add_command(label="Сохранить файл...", command=lambda: save_file(textbox))
    looks_menu = Menu(menu, tearoff=False)
    looks_menu.add_command(label="Увеличить шрифт", command=lambda: add_font_size(textbox))
    looks_menu.add_command(label="Уменьшить шрифт", command=lambda: minus_font_size(textbox))
    looks_menu.add_command(label="Темная тема", command=lambda: dark_mode(textbox))
    looks_menu.add_command(label="Светлая тема", command=lambda: light_mode(textbox))
    looks_menu.add_command(label="Сменить тему", command=lambda: swap_theme(textbox))
    syntax_menu = Menu(master=menu, tearoff=False)
    syntax_menu.add_command(label="Нет", command=lambda: syntax_configure(textbox, "None"))
    syntax_menu.add_command(label="C++", command=lambda: syntax_configure(textbox, "Cpp"))
    menu.add_cascade(label="Файл", menu=file_menu)
    menu.add_cascade(label="Внешний вид", menu=looks_menu)
    menu.add_cascade(label="Синтаксис", menu=syntax_menu)
    # сочетания клавиш
    window.bind_all("<Control-Key-s>", lambda e: save_file(textbox))
    window.bind_all("<Control-Key-o>", lambda e: open_file(textbox))
    window.bind_all("<Control-Key-0>", lambda e: add_font_size(textbox))
    window.bind_all("<Control-Key-9>", lambda e: minus_font_size(textbox))
    window.bind_all("<Control-Key-7>", lambda e: swap_theme(textbox))
    window.config(menu=menu)
    window.mainloop()
