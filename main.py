from tkinter import *
from tkinter import messagebox


def calculate():
    count1 = int(count1_tf.get())
    count2 = int(count2_tf.get()) / 100



window = Tk()
window.title('Калькулятор')
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

count1_lb = Label(
    frame,
    text="Введите первое число"
)
count1_lb.grid(row=3, column=1)

count2_lb = Label(
    frame,
    text="Введите второе число",
)
count2_lb.grid(row=4, column=1)

count1_tf = Entry(
    frame,
)
count1_tf.grid(row=3, column=2, pady=5)

count2_tf = Entry(
    frame,
)
count2_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Вычислить',

)
cal_btn.grid(row=5, column=2)

window.mainloop()

answer_lb = Label(
    frame,
)