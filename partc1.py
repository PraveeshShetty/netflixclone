from tkinter import *
from tkinter import messagebox

def clear_all():
    citxt.configure(state='normal')
    ptxt.delete(0,END)
    ttxt.delete(0,END)
    rtxt.delete(0,END)
    citxt.delete(0,END)
    ptxt.focus_set()

def calculate_ci():
    if not ptxt.get() or not ttxt.get() or not rtxt.get():
        messagebox.showinfo("information","information")
    else:
        p=int(ptxt.get())
        t=int(ttxt.get())
        r=int(rtxt.get())
        ci=(p*(pow((1+r/100),t)))
citxt.insert(0,CI)
citxt.configure('disabled')

root=tk()
root.configure(background='lavender')
root.geometry("400x250")
root.title("Compund Interest Calculation")

lp=label(root,text="Pricipal amount(Rs):",fg='white',bg='black')
lt=label(root,text="Time(year):",fg='white',bg='black')
lr=label(root,text="Rate(%):",fg='white',bg='black')
lci=label(root,text="compound interest:",fg='white',bg='black')

lp.grid(row=1,column=0,padx=10,pady=10)
lt.grid(row=2,column=0,padx=10,pady=10)
lr.grid(row=3,column=0,padx=10,pady=10)
lci.grid(row=5,column=0,padx=10,pady=10)

ptxt=Entry(root)
rtxt=Entry(root)
rtxt=Entry(root)
citxt=Entry(root)

ptxt.grid(row=1,column=1,padx=10,pady=10)
ttxt.rid(row=2,column=1,padx=10,pady=10)
rtxt.grid(row=3,column=1,padx=10,pady=10)
citxt.grid(row=5,column=1,padx=10,pady=10)

button1=Button(root.text="submit",bg='black',fg='white',command=calculate_ci)
button2=Button(root.text="clear",bg='black',fg='white',command=clear_all)

button1.grid(row=4,column=1,pady=10)
button2.grid(row=6,column=1,pady=10)
root.mainloop()



