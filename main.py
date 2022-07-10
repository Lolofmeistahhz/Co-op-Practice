from tkinter import Tk, Text, Menu

from config import open_file, save_file, add_font_size, minus_font_size
window = Tk()

if __name__ == "__main__":
    window.title('Блокнот')
    window.geometry("600x400")
    window.iconbitmap("favicon.ico")
    # внешний вид
    textbox = Text(master=window, yscrollcommand=True, font=('Consolas',12))
    textbox.pack(expand=True, fill="both")
    menu = Menu(window)
    file_menu = Menu(master=menu, tearoff=False)
    file_menu.add_command(label='Открыть файл...', command=lambda: open_file(textbox))
    file_menu.add_command(label="Сохранить файл...", command=lambda: save_file(textbox))
    looks_menu = Menu(menu, tearoff=False)
    looks_menu.add_command(label="Увеличить шрифт", command=lambda: add_font_size(textbox))
    looks_menu.add_command(label="Уменьшить шрифт", command=lambda: minus_font_size(textbox))
    looks_menu.add_command(label="Сменить тему...", command=lambda: print("test only"))
    menu.add_cascade(label="Файл", menu=file_menu)
    menu.add_cascade(label="Внешний вид", menu=looks_menu)
    # сочетания клавиш
    window.bind_all("<Control-Key-s>", lambda e: save_file(textbox))
    window.bind_all("<Control-Key-o>", lambda e: open_file(textbox))
    window.bind_all("<Control-Key-+>", lambda e: add_font_size(textbox))
    window.bind_all("<Control-Key-->", lambda e: minus_font_size(textbox))

    window.config(menu=menu)
    window.mainloop()