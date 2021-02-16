import tkinter as tk
import random
import tkinter.messagebox as mb

w = 200
number = 9
step = 0

def check_number():
    global number, step
    step = step + 1
    num = int(user_number.get())
    if num > number:
        lbl_answer.config(text="меньше")
    elif num < number:
        lbl_answer.config(text="больше")
    else:
        if step > 7:
            lbl_answer.config(text="Долго угадываешь")
        else:
            lbl_answer.config(text="УГАДАЛ!")
        step = 0
        number = random.randint(1, 101)
        mb.showinfo("Новая игра","Я загадал новое число")
        lbl_answer.config(text="Здесь будет подсказка")
        

win = tk.Tk()
win.title("Игра УГАДАЙ ЧИСЛО")
win.config(bg="green")
win.geometry("400x300")


lbl1 = tk.Label(text="Давай число", font=18, bg="green")
lbl1.place(x=100, y=10, width=w)

user_number = tk.Entry()
user_number.config(font=18)
user_number.place(x=100, y=40, width=w)

btn_check = tk.Button(text="Проверить", command=check_number, font=18)
btn_check.place(x=100, y=80, width=w)

lbl_answer = tk.Label(text="тут будет подсказка",font=18)
lbl_answer.place(x=100, y=110, width=w)

lbl_step = tk.Label(text="Количество попыток: 0", font=18)
lbl_step.place(x=100, y=140, width=w)


win.mainloop()