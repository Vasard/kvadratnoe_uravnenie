from tkinter import *
from math import *

def lahenda():
    
    if (a.get()!="" and b.get()!="" and c.get()!=""):#get-заполненность
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
        D=b_**2-4*a_*c_
        if D>0:
            x1_=(-1*b_+sqrt(D))/(2*a_)
            x2_=(-1*b_-sqrt(D))/(2*a_)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_=(-1*b_)/(2*a_)
            t=f"X1={x1_}"
        else:
            t="Корней нет"
        vastus.configure(text=f"D={D}\n{t}")
    else:     
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")

aken=Tk()
aken.geometry("600x300")#ширина х высота

lbl=Label(aken, text="Решение квадратного уравнения: ",font="Calibri 26", fg="red", bg="lightblue")
lbl.pack()
vastus=Label(aken, height=4, width=40, bg="yellow")
vastus.pack(side=BOTTOM)
a=Entry(aken, font="Calibri 26", fg="green", bg="lightblue", width=3)
a.pack(side=LEFT)#pack-отображает a
x2=Label(aken, text="x**2+", font="Calibri 26", fg="green", bg="lightblue")
x2.pack(side=LEFT)#pack-отображает х2
b=Entry(aken, font="Calibri 26", fg="green", bg="lightblue", width=3)
b.pack(side=LEFT)#pack-отображает b
x=Label(aken, text="x+", font="Calibri 26", fg="green", bg="lightblue")
x.pack(side=LEFT)#pack-отображает х
c=Entry(aken, font="Calibri 26", fg="green", bg="lightblue", width=3)
c.pack(side=LEFT)#pack-отображает c
y=Label(aken, text="=0", font="Calibri 26", fg="green", bg="lightblue")
y.pack(side=LEFT)#pack-отображает y


btn=Button(aken, text="Решить", font="Calibri 26", fg="blue", bg="lightblue", command=lahenda)
btn.pack(side=LEFT)#pack-отображает кнопку




aken.mainloop()

