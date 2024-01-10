from tkinter import *
# for jpg images 
from PIL import Image, ImageTk

intro_root = Tk()
intro_root.geometry("900x300")
intro_root.minsize(400,300)

l1=Label(text="Hello This is my first tk proj..")
l1.pack()

p1=PhotoImage(file="icon.png")
l2=Label(image=p1)
# l2.pack()

intro_root.title('Introduction to Tk')

# Important Label Options
# text -adds text
# bd - background
# fg - foreground
# padx -x padding
# pady - y padding
# font-font=("comicsans",19,"bold") or font=(comicsans 19 bold)
# relief - border styling -SUNKEN, RAISED, GROOVE,RIDGE

l3=Label(text='''
It looks like you've started creating a simple Tkinter \n
\napplication in Python. The code you provided initializes a \nTkinter window (intro_root) and starts the main event loop, \nallowing the window to be displayed and respond to user \ninteractions. However, your code is missing any content or \nwidgets within the window. To create a more meaningful \napplication, you can add various widgets like labels, \nbuttons, or entry fields.''',bg="red",fg="black",padx=24,pady=10,font=("comicsans",9,"bold"),borderwidth=10,relief=GROOVE
)

# Important pack attributes
# anchor = nw ne se sw
# side = top bottom left right
# fill, padx pady

# l3.pack(side="bottom",anchor="se",fill=X)
l3.pack(side="left",anchor="se",fill=Y,padx=10,pady=30)


intro_root.mainloop()
