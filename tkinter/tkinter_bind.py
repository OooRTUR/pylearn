from tkinter import *

root = Tk()


def change_on_enter(event):
    b['fg'] = "red"
    b['activeforeground'] = "red"

def change_on_click(event):
    b['fg'] = "green"
    b['activeforeground'] = "black"

b = Button(text='RED', width=10, height=3)
b.bind('<Button-1>', change_on_click)
b.bind('<Return>', change_on_enter)

b.pack()

root.mainloop()
