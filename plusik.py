import tkinter as tk
import tkinter.messagebox as mb

start = 1

def click_plus(e):
    global start
    start = start + 1
    lbl_start.config(text=str(start))
    if start > 15:
        mb.showinfo("Информация", "Перебор!")
        start = 1
        lbl_start.config    (text=str(start))
    
def click_mult(e):
    global start
    start = start * 2
    lbl_start.config(text=str(start))
    if start > 15:
        mb.showinfo("Информация", "Перебор!")
        start = 1
        lbl_start.config(text=str(start))
        
win = tk.Tk()
win.geometry("800x400")
win.title("ИГРА плюсик и умножик")

btn_plus = tk.Button(text="+1", font=("Aria", "50"), bg="#FF0000")
btn_plus.place(x=100, y=100, width=130, height=130)
btn_plus.bind('<Button-1>', click_plus)

btn_mult = tk.Button(text="x2", font=("Aria", "50"), bg="#00FF00")
btn_mult.place(x=570, y=100, width=130, height=130)
btn_mult.bind('<Button-1>', click_mult)

lbl_start = tk.Label(text="1", font=("Aria", "50"), bg="#FFFFFF")
lbl_start.place(x=400, y=250)

lbl_finish = tk.Label(text="15", font=("Aria", "50"), bg="#FFFFFF")
lbl_finish.place(x=380, y=50)

win.mainloop()



