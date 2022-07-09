from tkinter import Tk, Text, Menu
import config
if __name__ == "__main__":
    window = Tk()
    window.title('Блокнот')
    window.geometry("600x400")
    textbox = Text(yscrollcommand=True, font=('Consolas',12))
    textbox.pack(expand=True, fill="both")
    menu = Menu(window)
    # textbox.configure(font=())

    file_menu = Menu(menu, tearoff=False)
    file_menu.add_command(label='Открыть файл...', command=lambda: config.open_file(textbox))
    file_menu.add_command(label="Сохранить файл...", command=lambda: config.save_file(textbox))
    menu.add_cascade(label="Файл", menu=file_menu)
    window.config(menu=menu)
    window.mainloop()