from tkinter import  *
root = Tk()

r_var = IntVar()
r_var.set(0)

r1 = Radiobutton(text='First', variable=r_var, value=0)
r2 = Radiobutton(text='Second', variable=r_var, value=1)
r3 = Radiobutton(text='Third', variable=r_var, value=2)

r1.pack(anchor=W)
r2.pack(anchor=W)
r3.pack(anchor=W)

root.mainloop()