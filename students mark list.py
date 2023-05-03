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
lb4=Label(w,text='Marks',font=10,bg='black',fg='white',width=20).place(x=170,y=130)

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

maths10=Entry(w,highlightthickness=1,highlightbackground='black',width=25)
maths10.place(x=315,y=220)




def display():
    
    lb0=Label(w,text='Subject',font=10,bg='red',fg='white',width=15)
    lb0.place(x=60,y=460)
    lb1=Label(w,text='Marks',font=10,bg='red',fg='white',width=15)
    lb1.place(x=200,y=460)
    lb2=Label(w,text='Grade',font=10,bg='red',fg='white',width=15)
    lb2.place(x=330,y=460)
    
    
    lb3=Label(w,text="Stud Name : "+en.get(),bg='grey',fg='black',font=15)
    lb3.place(x=25,y=330)

    lb4=Label(w,text='Enroll No : '+en2.get(),bg='grey',fg='black',font=15)
    lb4.place(x=25,y=360)
    
 
    lb6=Label(w,text='ENGLISH',bg='red',fg='white',width=15,highlightthickness=1,highlightbackground='black')
    lb6.place(x=60,y=484)
    lb61=Label(w,text=english3.get(),bg='white',fg='red',width=25,highlightthickness=1,highlightbackground='black')
    lb61.place(x=172,y=484)
    lb62=Label(w,text=english4.get(),bg='white',fg='red',width=21,highlightthickness=1,highlightbackground='black')
    lb62.place(x=315,y=484)

    lb7=Label(w,text='HINDI',bg='red',fg='white',width=15,highlightthickness=1,highlightbackground='black')
    lb7.place(x=60,y=506)
    lb71=Label(w,text=hindi5.get(),bg='white',fg='red',width=25,highlightthickness=1,highlightbackground='black')
    lb71.place(x=172,y=506)
    lb72=Label(w,text=hindi6.get(),bg='white',fg='red',width=21,highlightthickness=1,highlightbackground='black')
    lb72.place(x=315,y=506)

    lb8=Label(w,text='SCIENCE',bg='red',fg='white',width=15,highlightthickness=1,highlightbackground='black')
    lb8.place(x=60,y=528)
    lb81=Label(w,text=science7.get(),bg='white',fg='red',width=25,highlightthickness=1,highlightbackground='black')
    lb81.place(x=172,y=528)
    lb82=Label(w,text=science8.get(),bg='white',fg='red',width=21,highlightthickness=1,highlightbackground='black')
    lb82.place(x=315,y=528)

    lb9=Label(w,text='MATHS',bg='red',fg='white',width=15,highlightthickness=1,highlightbackground='black')
    lb9.place(x=60,y=550)
    lb91=Label(w,text=maths9.get(),bg='white',fg='red',width=25,highlightthickness=1,highlightbackground='black')
    lb91.place(x=172,y=550)
    lb92=Label(w,text=maths10.get(),bg='white',fg='red',width=21,highlightthickness=1,highlightbackground='black')
    lb92.place(x=315,y=550)
     

    lb10=Label(w,text='GRADE CARD',bg='green',fg='white',font=15)
    lb10.place(x=25,y=390)
    lb11=Label(w,text='out of 400',bg='grey',fg='black',font=15)
    lb11.place(x=25,y=420)

    lb11=Label(w,text='YOUR TOTAL SCORE :',bg='grey',fg='black')
    lb11.place(x=25,y=600)
    lb12=Label(w,text=int(english3.get())+int(hindi5.get())+int(science7.get())+int(maths9.get()))
    lb12.place(x=150,y=600)

    lb13=Label(w,text='PERCENTAGE OBTAINED :',bg='grey',fg='black')
    lb13.place(x=25,y=630)
    sum=int(english3.get())+int(hindi5.get())+int(science7.get())+int(maths9.get())
    result=sum*100
    s=result/400
    lb14=Label(w,text=s)
    lb14.place(x=172,y=630)


bt=Button(text='LOGIN',command=display,bg='red',fg='white',width=15)
bt.place(x=355,y=250)

w.mainloop() 
