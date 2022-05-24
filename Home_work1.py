from tkinter import *
from tkinter import ttk

def nazmy():
    print("Все работает хорошо")

root = Tk()  # инициализация инстанса - создание объекта ткинтер

frm = ttk.Frame(root, padding=10)  # создание главного окна, padding размер окна
root.title("большая кнопка")
root.geometry("640x480")  # размер окна
frm.grid()  # решетка, сетка

Button(text="это кнопка",  # текст кнопки
       background="#B22222",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=nazmy).grid(column=3, row=5)


root.mainloop()
