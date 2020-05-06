from tkinter import *
root = Tk()
f_top = LabelFrame(root,text="Top")
f_bot = LabelFrame(root,text="Bottom")

l1 = Label(f_top, width=7, height=4, bg='yellow', text="1")
l2 = Label(f_top, width=7, height=4, bg='orange', text="2")
l3 = Label(f_bot, width=7, height=4, bg='lightgreen', text="3")
l4 = Label(f_bot, width=7, height=4, bg='lightblue', text="4")

f_top.pack(padx=10, pady=10, ipadx=10, ipady=10)
f_bot.pack(padx=10, pady=10, ipadx=10, ipady=10)
l1.pack(side=LEFT)
l2.pack(side=RIGHT)
l3.pack(side=LEFT)
l4.pack(side=RIGHT)

root.mainloop()