from tkinter import *


def btn_click():
    mark = 0
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 3
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 3
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 3
    if v5.get() == 1:
        mark += 3
    if v7.get() == 2:
        mark += 2
    if chb7.get() == '1991':
        mark += 2
    if v9.get() == 1 and v10.get() == 1 and v11.get() == 1 and v12.get() == 1:
        mark += 2
    elif v9.get() == 0 and v10.get() == 1 and v11.get() == 1 and v12.get() == 1:
        mark += 2
    elif v9.get() == 1 and v10.get() == 0 and v11.get() == 1 and v12.get() == 1:
        mark += 2
    elif v9.get() == 1 and v10.get() == 1 and v11.get() == 0 and v12.get() == 1:
        mark += 2
    elif v9.get() == 1 and v10.get() == 1 and v11.get() == 1 and v12.get() == 0:
        mark += 2
    elif v9.get() == 1 and v10.get() == 1 and v11.get() == 0 and v12.get() == 0:
        mark += 1
    elif v9.get() == 0 and v10.get() == 0 and v11.get() == 1 and v12.get() == 1:
        mark += 1
    elif v9.get() == 1 and v10.get() == 0 and v11.get() == 1 and v12.get() == 0:
        mark += 1
    elif v9.get() == 0 and v10.get() == 1 and v11.get() == 0 and v12.get() == 1:
        mark += 1

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
v7 = IntVar()
chb5 = Radiobutton(tk, text="Компільована", variable=v7, value=1)
chb6 = Radiobutton(tk, text="Інтерпритована", variable=v7, value=2)

lbl7 = Label(tk, text="Питання №4", font=font_title)
lbl8 = Label(tk, text="У якому році було опубліковано 3 версію Python?", font=font_q)
chb7 = Entry(tk)

lbl9 = Label(tk, text="Питання №5", font=font_title)
lbl10 = Label(tk, text="Які є різновиди Python?", font=font_q)
v9 = IntVar()
v10 = IntVar()
v11 = IntVar()
v12 = IntVar()
chb8 = Checkbutton(tk, text="CPython", variable=v9, onvalue=1, offvalue=0)
chb9 = Checkbutton(tk, text="RustPython", variable=v10, onvalue=1, offvalue=0)
chb10 = Checkbutton(tk, text="Jython", variable=v11, onvalue=1, offvalue=0)
chb11 = Checkbutton(tk, text="IronPython", variable=v12, onvalue=1, offvalue=0)


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
chb6.pack()

lbl7.pack()
lbl8.pack()
chb7.pack()

lbl9.pack()
lbl10.pack()
chb8.pack()
chb8.pack()
chb9.pack()
chb10.pack()
chb11.pack()


btn.pack()
result.pack()

tk.mainloop()

