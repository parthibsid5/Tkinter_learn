from tkinter import *
root=Tk()
root.geometry("655x333")
f1=Frame(root, bg="blue",borderwidth=5)
f1.pack(side="top")

p1=PhotoImage(file="icon.png")
l2=Label(image=p1)
l2.pack(side=LEFT)

l2=Label(f1,text="This is a news article.. ",bg="red")
l2.pack()

root.mainloop()