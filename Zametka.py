from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

note_name = NONE  # имя заметки


class Main:

    @staticmethod
    def new_note():  # метод создания новой заметки
        global note_name
        note_name = 'Без названия'
        text.delete('1.0', END)  # очистка от возможного текста

    @staticmethod
    def open_note():  # метод открытия новой заметки
        global note_name
        note = askopenfile(mode='r')  # вызов диалогового окна с выбором файла
        data = note.read()
        text.delete('1.0', END)  # очистка от существующего текста
        text.insert('1.0', data)  # ввод текста из открытой заметки

    @staticmethod
    def save_note():
        out = asksaveasfile(mode='w', defaultextension='.txt')  # вызов диалогового окна для сохранения заметки
        data = text.get('1.0', END)
        out.write(data.rstrip())  # запись заметки


root = Tk()
root.title('Notes')
root.geometry('640x480')

text = Text(root, width=300, height=300)
text.pack()
text.config(font=('TimesNewRoman', 18))

menu_bar = Menu(root)
note_menu = Menu(menu_bar)

menu_bar.add_cascade(label='Note', menu=note_menu)
note_menu.add_command(label='Open', command=Main.open_note)
note_menu.add_command(label='Save', command=Main.save_note)
note_menu.add_command(label='New', command=Main.new_note)

root.config(menu=menu_bar)
root.mainloop()
