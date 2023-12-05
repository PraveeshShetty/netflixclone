from tkinter import *
def buttonClick(self):
    print('you have clicked me')

root=Tk()
f=Frame(root,height=200,width=300)
f.propagate(0)
f.pack()

b=Button(f, text='My button', width=15, height=2, bg='yellow', fg='blue', activebackground='green', activeforeground='red')
b.pack()
b.bind(" <Button-1>",buttonClick)
root.mainloop()
