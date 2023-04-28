from tkinter import *

w = Tk() 
w.title("LOGIN FORM") 
w.configure(background='black')
w.geometry('400x250')
lb=Label(w,text='LOGIN FORM',bg='red',fg='white').place(x=30,y=10)

lb=Label(w,text='USERNAME',font=10,bg='green',fg='white').place(x=30,y=40)

lb2=Label(w,text='PASSWORD',font=10,bg='green',fg='white')
lb2.place(x=30,y=70)

en=Entry(w)
en.place(x=150,y=40)

en2=Entry(w)
en2.place(x=150,y=70)

def display():
    lb3=Label(w,text=en.get(),bg='black',fg='white',font=20)
    lb3.place(x=150,y=130)

    lb4=Label(w,text=en2.get(),bg='black',fg='white',font=20)
    lb4.place(x=150,y=160)

bt=Button(text='LOGIN',command=display)
bt.place(x=150,y=100)

w.mainloop() 