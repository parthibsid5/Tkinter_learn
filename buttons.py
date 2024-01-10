from tkinter import *
root=Tk()
root.geometry("400x500")

root.title("Servo rotation button ")
def but1():
    print("Servo rotated to 0 degree")
f1=Frame(root,bg="black",borderwidth=5)
f1.pack(side="left",anchor="nw")
b1=Button(f1,text="0º",command=but1)
b1.pack()

def but2():
    print("Servo rotated to 45 degree")
f2=Frame(root,bg="black",borderwidth=5)
f2.pack(side="left",anchor="nw")
b2=Button(f2,text="45º",command=but2)
b2.pack()

def but3():
    print("Servo rotated to 90 degree")
f3=Frame(root,bg="black",borderwidth=5)
f3.pack(side="left",anchor="nw")
b3=Button(f3,text="90º",command=but3)
b3.pack()

def but4():
  print("Servo rotated to 135 degree")
f4=Frame(root,bg="black",borderwidth=5)
f4.pack(side="left",anchor="nw")
b4=Button(f4,text="135º",command=but4)
b4.pack()

def but5():
    print("Servo rotated to 180 degree")
f5=Frame(root,bg="black",borderwidth=5)
f5.pack(side="left",anchor="nw")
b5=Button(f5,text="180º",command=but5)
b5.pack()

root.mainloop()