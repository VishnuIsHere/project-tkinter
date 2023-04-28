from tkinter import *

w = Tk() 
w.title("Students Mark List") 
w.configure(background='grey')
w.geometry('550x800')
lb0=Label(w,text='STUDENT MARK LIST',bg='red',fg='white').place(x=30,y=10)

lb=Label(w,text='NAME',font=10,bg='green',fg='white').place(x=30,y=70)

lb2=Label(w,text='Enroll No:',font=10,bg='green',fg='white')
lb2.place(x=250,y=70)
lb3=Label(w,text='Subject',font=10,bg='black',fg='white',width=15).place(x=60,y=130)
lb4=Label(w,text='Marks',font=10,bg='black',fg='white',width=15).place(x=200,y=130)
lb5=Label(w,text='Grade',font=10,bg='black',fg='white',width=15).place(x=330,y=130)
lb6=Label(w,text='ENGLISH',bg='white',fg='black',width=15,highlightthickness=1,highlightbackground='black').place(x=60,y=153)
lb7=Label(w,text='HINDI',bg='white',fg='black',width=15,highlightthickness=1,highlightbackground='black').place(x=60,y=175)
lb8=Label(w,text='SCIENCE',bg='white',fg='black',width=15,highlightthickness=1,highlightbackground='black').place(x=60,y=197)
lb9=Label(w,text='MATHS',bg='white',fg='black',width=15,highlightthickness=1,highlightbackground='black').place(x=60,y=219)


en=Entry(w)
en.place(x=100,y=70)

en2=Entry(w)
en2.place(x=350,y=70)

english3=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
english3.place(x=172,y=153)

english4=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
english4.place(x=315,y=153)

hindi5=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
hindi5.place(x=172,y=176)

hindi6=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
hindi6.place(x=315,y=176)

science7=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
science7.place(x=172,y=198)

science8=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
science8.place(x=315,y=198)

maths9=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
maths9.place(x=172,y=220)

maths8=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
maths8.place(x=315,y=220)




def display():
    
    lb0=Label(w,text='Subject',font=10,bg='black',fg='white',width=15)
    lb0.place(x=60,y=460)
    lb1=Label(w,text='Marks',font=10,bg='black',fg='white',width=15)
    lb1.place(x=200,y=460)
    lb2=Label(w,text='Grade',font=10,bg='black',fg='white',width=15)
    lb2.place(x=330,y=460)
    
    
    lb3=Label(w,text="Stud Name : "+en.get(),bg='grey',fg='black',font=15)
    lb3.place(x=25,y=330)

    lb4=Label(w,text='Enroll No : '+en2.get(),bg='grey',fg='black',font=15)
    lb4.place(x=25,y=360)
    
    lb6=Label(w,text=english3.get(),bg='grey',fg='black',width=25,highlightthickness=1,highlightbackground='black')
    lb6.place(x=172,y=484)
    lb61=Label(w,text='ENGLISH',bg='grey',fg='black',width=15,highlightthickness=1,highlightbackground='black')
    lb61.place(x=60,y=484)
    lb62=Label(w,text=english4.get(),bg='grey',fg='black',width=21,highlightthickness=1,highlightbackground='black')
    lb62.place(x=315,y=484)

    lb7=Label(w,text='HINDI',bg='white',fg='black',width=15,highlightthickness=1,highlightbackground='black')
    lb7.place(x=60,y=506)
    lb71=Label(w,text=hindi5.get(),bg='grey',fg='black',width=25,highlightthickness=1,highlightbackground='black')
    lb71.place(x=172,y=506)

    lb8=Label(w,text='SCIENCE',bg='white',fg='black',width=15,highlightthickness=1,highlightbackground='black').place(x=60,y=197)
    lb9=Label(w,text='MATHS',bg='white',fg='black',width=15,highlightthickness=1,highlightbackground='black').place(x=60,y=219)
    ib10=Label(w,text='GRADE CARD',bg='grey',fg='black',font=15)
    ib10.place(x=25,y=390)
    ib11=Label(w,text='out of 400',bg='grey',fg='black',font=15)
    ib11.place(x=25,y=420)

    
    # en2=Entry(w)
    # en2.place(x=350,y=70)

    # english3=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # english3.place(x=172,y=153)

    # english4=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # english4.place(x=315,y=153)

    # hindi5=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # hindi5.place(x=172,y=176)

    # hindi6=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # hindi6.place(x=315,y=176)

    # science7=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # science7.place(x=172,y=198)

    # science8=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # science8.place(x=315,y=198)

    # maths9=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # maths9.place(x=172,y=220)

    # maths8=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
    # maths8.place(x=315,y=220)


bt=Button(text='LOGIN',command=display,bg='red',fg='white',width=15)
bt.place(x=355,y=250)

w.mainloop() 
