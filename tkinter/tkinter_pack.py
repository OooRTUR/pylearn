from tkinter import *

root = Tk()
l1 = Label(width=7, height=4, bg='yellow', text="1")
l2 = Label(width=7, height=4, bg='orange', text="2")
l3 = Label(width=7, height=4, bg='lightgreen', text="3")
l4 = Label(width=7, height=4, bg='lightblue', text="4")

l1.pack(side=TOP)
l4.pack(side=BOTTOM)    
l2.pack(side=LEFT)
l3.pack(side=RIGHT)


root.mainloop()