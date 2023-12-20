from tkinter import *
from tkinter import ttk


def btn_click():
    mark = 0
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 2
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    if v5.get() == 1:
        mark += 2
    if v7.get() == "Інтерпритована":
        mark += 2
    if chb7.get() == 2008:
        mark += 2
    if v9.get() == 'CPython':
        mark += 2
    if v10.get() == 'Гвідо Ван Россум':
        mark += 2

    if mark > 6:
        result["fg"] = "green"
    else:
        result["fg"] = "red"
    v6.set("Ваша оцінка: "+str(mark))


tk = Tk()
tk.title("Тест з інформатики")
font_title = ("Arial", 14, "bold")
font_q = ("Arial", 12, "bold")
lbl1 = Label(tk, text="Питання №1", font=font_title)
lbl2 = Label(tk, text="Які існують пристрої введення?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Клавіатура", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Миша", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Монітор", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Принтер", variable=v4, onvalue=1, offvalue=0)

lbl3 = Label(tk, text="Питання №2", font=font_title)
lbl4 = Label(tk, text="Скільки Мб у Гб?", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="1024", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="1000", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="8", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="1000000", variable=v5, value=4)

lbl5 = Label(tk, text="Питання №3", font=font_title)
lbl6 = Label(tk, text="Якого типу мова програмування Python?", font=font_q)
v7 = StringVar()
v7.set("Інтерпритована")
chb5 = OptionMenu(tk, v7, "Інтерпритована", "Компільована")

lbl7 = Label(tk, text="Питання №4", font=font_title)
lbl8 = Label(tk, text="У якому році було опубліковано 3 версію Python?", font=font_q)
chb7 = Scale(tk, from_=1991, to=2023, tickinterval=1, orient=HORIZONTAL)

lbl9 = Label(tk, text="Питання №5", font=font_title)
lbl10 = Label(tk, text="Який різновид Python з'явився першим?", font=font_q)
lbl1212 = Label(tk, text="CPython, RustPython, Jython чи IronPython", font=font_q)
v9 = Entry(tk)

lbl11 = Label(tk, text="Питання №6", font=font_title)
lbl12 = Label(tk, text="Як звати автора Python?", font=font_q)

v10 = ttk.Combobox(tk, values=["Бьйорн Страуструп", "Брендан Ейх", "Гвідо Ван Россум", "Денніс Рітчі"])

v6 = StringVar()
btn = Button(tk, text="Відповісти", command=btn_click, font=font_q)
result = Label(tk, text='', textvariable=v6, font=font_title)

lbl1.pack()
lbl2.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()
lbl3.pack()
lbl4.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()

lbl5.pack()
lbl6.pack()
chb5.pack()

lbl7.pack()
lbl8.pack()
chb7.pack()

lbl9.pack()
lbl10.pack()
lbl1212.pack()
v9.pack()

lbl11.pack()
lbl12.pack()
v10.pack()





btn.pack()
result.pack()

tk.mainloop()
