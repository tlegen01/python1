# #импорт всей библиотеки
# import time
# # использование одного метода из этой библиотеки
# time.sleep(secs=0.0001)

# from tkinter import * #импорт всех функций, классов из библиотеки ! Может вызвать коллизию имен !

# import tkinter as tk #Импорт всей библиотеки с присфоением псевдонима для дальнейшего вызова

# from.calc import calc_3 #импорт одной функции
# calc_3

# from.import calc #импорт своей функций
# calc.result


# импортируем бибилиотеку для работы с окнами (интерфейсом) все библиотеки:   tkinter pyqt5 pyside6
# tkinter pyqt5 pyside6
# tkinter входит в стандартную библиотеку python устанавливать не надо


from tkinter import *
from tkinter import ttk
import time
from threading import Thread

hours = 0
minutes = 0
seconds = 0

pause = True

def stop_timer():
    global pause
    pause = False

def reset_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0
    hours_lable.config(text=f"{hours}")
    minutes_lable.config(text=f"{minutes}")
    seconds_lable.config(text=f"{seconds}")

def start_timer():
    global  pause
    pause = True

    global hours
    # hours = 0
    global minutes
    # minutes = 0
    global seconds
    # seconds = 0


    while pause:
        seconds += 1
        if seconds > 59:
            minutes += 1
            seconds = 0
            if minutes > 59:
                hours += 1
                minutes = 0
                if hours > 23:
                    seconds = 0
                    minutes = 0
                    hours = 0
        time.sleep(0.0001)
        hours_lable.config(text=f"{hours}")
        minutes_lable.config(text=f"{minutes}")
        seconds_lable.config(text=f"{seconds}")
        print(f"{hours}:{minutes}:{seconds}")

def start_new_thread():
    Thread(target=start_timer).start()  # используется для вызова
# функции в отдельный поток, тогда остальная часть окна не будет виснуть

root = Tk()  # инициализация инстанса - создание объекта ткинтер

frm = ttk.Frame(root, padding=10)  # создание главного окна, padding размер окна
root.title("Таймер с интерфейсом на Python")
root.geometry("640x480")  # размер окна
frm.grid()  # решетка, сетка

# 0    1    2     3    4      5
# 1   Any    :   Alex  :     Ivan

hours_lable = ttk.Label(frm, text="00")  # сроки и столбцы
hours_lable.grid(column=0, row=0)

ttk.Label(frm, text=":").grid(column=1, row=0)  # сроки и столбцы

minutes_lable=ttk.Label(frm, text="00")  # сроки и столбцы
minutes_lable.grid(column=2, row=0)

ttk.Label(frm, text=":").grid(column=3, row=0)  # сроки и столбцы

seconds_lable = ttk.Label(frm, text="00")       # сроки и столбцы
seconds_lable.grid(column=4, row=0)             # сроки и столбцы


Button(text="stop",  # текст кнопки  #  кнопка стоп
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=stop_timer).grid(column=0, row=1) #ссылка на функцию

Button(text="reset",  # текст кнопки  #  кнопка reset
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=reset_timer).grid(column=1, row=1)


Button(text="start",  # текст кнопки  #  кнопка стоп # кнопка старт
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=start_new_thread).grid(column=2, row=1)

root.mainloop()  # основной цикл событий





