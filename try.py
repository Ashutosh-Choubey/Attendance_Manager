from tkinter import *
root=Tk()
l=Label(root,text="hello",width=5,height=10)
print(l.cget("text"))
l['text']='world'
l.pack()
root.mainloop()