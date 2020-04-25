from tkinter import *

root = Tk()

r_var = IntVar()
r_var.set(0)

data = [
    'some text',
    'and one another text',
    'ok'
]

def set_content():
    t['text'] = data[r_var.get()]

f_left = Frame(root,width=100)
f_right = Frame(root, width=200)



r1 = Radiobutton(f_left, variable=r_var,value=0, command=set_content, indicatoron=0,width=10)
r2 = Radiobutton(f_left, variable=r_var, value=1, command=set_content, indicatoron=0, width=10)
r3 = Radiobutton(f_left, variable=r_var, value=2, command=set_content, indicatoron=0, width=10)
t = Label(f_right, width=40)
set_content()



r1.pack()
r2.pack()
r3.pack()
t.pack()
f_left.pack(side=LEFT)
f_right.pack(side=LEFT)
root.mainloop()