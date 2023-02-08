from tkinter import *

import random

root = Tk()

root.title("Главное окно")
root.geometry('1280x720')

frame_widget = Frame(root)  # тут все кроме таблицы
frame_table = Frame(root)  # тут таблица

frame_widget.pack(side=LEFT)  # тут все кроме таблицы
frame_table.pack(side=LEFT)  # тут таблица

step_num = 0  # хранит текущий шаг
lst = []  # двумерный список где хранятся значения таблицы
break_num = 0  # хранит число сломанных вершин


def insert_1():  # функция вызывается при нажатии кнопки начать
    global step_num, lst, break_num

    for widget in frame_table.winfo_children():  # отчистка таблицы
        widget.destroy()

    step_num = 0
    break_num = 0

    mu = float(entry_2.get())  # Среднее значение
    sigma = float(entry_3.get())  # СКО

    lst = [[float(random.gauss(mu, sigma)) for j in range(int(entry_1.get()))] for i in
           range(int(entry_1.get()))]  # создаем двумерный список, который хранит значения ячеек

    for i in range(
            len(lst)):  # проходимся по двумерному списку и рисуем значения ячеек в виде Button на frame_table в метод grid передаем номер строки и столбца
        for j in range(len(lst)):
            Button(frame_table, bg='#E0FFFF', justify=CENTER, bd=4, fg='#000000', borderwidth=4, width=5, height=1,
                   text=str(round(lst[i][j], 1)), font="Arial 8").grid(row=i, column=j)

    label_5 = Label(frame_widget, text="Текущий шаг " + str(int(entry_4.get())),
                    font="Arial 16")  # показывает текущий шаг
    label_6 = Label(frame_widget, text="Число сломанных вершин " + str(break_num),
                    font="Arial 16")  # показываем число сломанных вершин

    label_5.grid(row=5, column=0)  # выводим с помощью grid текущий шаг
    label_6.grid(row=6, column=0)  # выводим с помощью grid число сломанных вершин


def insert_2():  # функция вызывается при нажатии кнопки продолжить
    global step_num, lst, break_num

    step_num += int(entry_4.get())  # увеличиваем шаг
    break_num = 0

    for i in range(len(lst)):  # проходимся по двумерному списку и красим ячейки если они ментше шага
        for j in range(len(lst)):
            if lst[i][j] < step_num:
                Button(frame_table, bg='#FF0000', justify=CENTER, bd=4, fg='#000000', borderwidth=4, width=5, height=1,
                       text=str(round(lst[i][j], 1)), font="Arial 8").grid(row=i, column=j)
                break_num += 1

    label_5 = Label(frame_widget, text="Текущий шаг " + str(step_num), font="Arial 16")  # показывает текущий шаг
    label_6 = Label(frame_widget, text="Число сломанных вершин " + str(break_num),
                    font="Arial 16")  # показываем число сломанных вершин

    label_5.grid(row=5, column=0)  # выводим с помощью grid текущий шаг
    label_6.grid(row=6, column=0)  # выводим с помощью grid число сломанных вершин


# дальше объявляем кнопки, поля, лейблы
label_1 = Label(frame_widget, text="Размер решетки", font="Arial 16")
label_2 = Label(frame_widget, text="Среднее значение", font="Arial 16")
label_3 = Label(frame_widget, text="Укажите СКО", font="Arial 16")
label_4 = Label(frame_widget, text="Укажите шаг", font="Arial 16")

entry_1 = Entry(frame_widget)
entry_2 = Entry(frame_widget)
entry_3 = Entry(frame_widget)
entry_4 = Entry(frame_widget)

button_1 = Button(frame_widget, text="Начало", command=insert_1)
button_2 = Button(frame_widget, text="Продолжить", command=insert_2)

label_5 = Label(frame_widget, text="Текущий шаг " + str(step_num), font="Arial 16")
label_6 = Label(frame_widget, text="Число сломанных вершин " + str(break_num), font="Arial 16")
# дальше выводить с помощью метода grid кнопки, поля, лейблы
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
label_3.grid(row=2, column=0)
label_4.grid(row=3, column=0)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)
entry_4.grid(row=3, column=1)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)

label_5.grid(row=5, column=0)
label_6.grid(row=6, column=0)

root.mainloop()
