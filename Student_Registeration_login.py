from tkinter import *
import math
import pymysql
import os
import tkinter as tk

#Record for Registration  
def check(lb,g,txt):
    user_info=username_entry.get()
    pwd_info=pwd_entry.get()
    name_info=name_entry.get()
    age_info=age_entry.get()
    cgpa_info=cgpa_entry.get()
    father_info=father_entry.get()
    if g.get()==1:
        gen="Male"
    else:
        gen="Female"
    t=scroll.get()
    conn=pymysql.connect(host="localhost",user="root",password="ansk27911",db="student")
    a=conn.cursor()
    sql="insert into student_register values('"+user_info+"','"+pwd_info+"')"
    a.execute(sql)
    conn.commit()
    sql="insert into student_info values('"+user_info+"','"+name_info+"','"+age_info+"','"+gen+"','"+father_info+"',"+cgpa_info+",'"+t+"')"
    a.execute(sql)
    conn.commit()
    lb.configure(text="Registration Successful",fg="green")
    


def academics():
    academics=Toplevel(w)
    academics.title("Academic Histroy")
    academics.iconbitmap(r'Student.ico')
    academics.attributes("-fullscreen", True)
    conn=pymysql.connect(host="localhost",user="root",password="ansk27911",db="student")
    a=conn.cursor()
    sql="select student_academics.sem1,student_academics.sem2,student_academics.sem3 from student_register inner join student_academics where student_register.username=student_academics.username and student_register.username='"+user1_info+"'"
    a.execute(sql)
    conn.commit()
    data=a.fetchall()
    for d in data:
        lb1=Label(academics,text="Semester1:  "+str(d[0]),font=("Calibri",20),fg="blue").place(x=300,y=30)
        lb2=Label(academics,text="Semester2:  "+str(d[1]),font=("Calibri",20),fg="blue").place(x=300,y=80)
        lb3=Label(academics,text="Semester3:  "+str(d[2]),font=("Calibri",20),fg="blue").place(x=300,y=130)
    Button(academics,text='View Sem1', command = lambda:os.startfile('Resume_anurag.pdf'),bd=5,width=13,font="14").place(x=300,y=180)


#Check For Login   
def check_login():
    check_login=Toplevel(w)
    check_login.title("Dashboard")
    check_login.geometry('300x300+200+200')
    check_login.iconbitmap(r'Student.ico')
    global user1_info
    user1_info=username1_entry.get()
    pwd1_info=pwd1_entry.get()
    user=username1_entry.get()
    conn=pymysql.connect(host="localhost",user="root",password="ansk27911",db="student")
    a=conn.cursor()
    sql="select student_info.username,student_info.name,student_info.age,student_info.gender,student_info.father_name,student_info.cgpa,student_info.address from student_register inner join student_info where student_register.username=student_info.username and student_register.username='"+user+"'"
    a.execute(sql)
    conn.commit()
    data=a.fetchall()
    i=2
    for d in data:
        lb1=Label(check_login,text="Username:"+d[0],font=("Calibri",20),fg="blue").place(x=300,y=30)
        lb2=Label(check_login,text="Name:"+d[1],font=("Calibri",20),fg="blue").place(x=300,y=80)
        lb3=Label(check_login,text="Age:"+str(d[2]),font=("Calibri",20),fg="blue").place(x=300,y=130)
        lb4=Label(check_login,text="Gender:"+str(d[3]),font=("Calibri",20),fg="blue").place(x=300,y=180)
        lb5=Label(check_login,text="Father Name:"+d[4],font=("Calibri",20),fg="blue").place(x=300,y=230)
        lb6=Label(check_login,text="CGPA:"+str(d[5]),font=("Calibri",20),fg="blue").place(x=300,y=280)
        lb7=Label(check_login,text="Address:"+d[6],font=("Calibri",20),fg="blue").place(x=300,y=330)
        i=i+1
    Button(check_login,text="Student Profile",bg="blue",fg="white").place(x=30,y=30)
    Button(check_login,text="Academic History",bg="blue",fg="white",command=lambda:[academics()]).place(x=30,y=80)
    Button(check_login,text="Change Password",bg="blue",fg="white").place(x=30,y=130)
    Button(check_login,text="Log Out",bg="blue",fg="white",command=lambda:[check_login.destroy(),login()]).place(x=30,y=180)




    
#Registration Details
def register():
    register=Toplevel(w)
    register.title("Register")
    register.geometry('300x300+200+200')
    register.iconbitmap(r'Student.ico')
    #set Variables
    global username
    global password
    global name
    global username_entry
    global pwd_entry
    global name_entry
    global age_entry
    global scroll
    global father_entry
    global cgpa_entry
    global gen1
    global gen2
    username=StringVar()
    password=StringVar()
    name=StringVar()
    father_name=StringVar()
    address=StringVar()
    txt=StringVar()
    cgpa=DoubleVar()
    age=IntVar()
    var=IntVar()
    Label(register,text="Please enter the details below",font=("Calibri",12)).pack()
    Label(register,text="").pack()
    username_label=Label(register,text="Username *")
    username_label.pack()
    username_entry=Entry(register,textvariable=username)
    username_entry.pack()
    pwd_label=Label(register,text="Password *")
    pwd_label.pack()
    pwd_entry=Entry(register,textvariable=password,show="*")
    pwd_entry.pack()
    name_label=Label(register,text="Name *")
    name_label.pack()
    name_entry=Entry(register,textvariable=name)
    name_entry.pack()
    age_label=Label(register,text="Age *")
    age_label.pack()
    age_entry=Entry(register,textvariable=age)
    age_entry.pack()
    Label(register,text="Gender *").pack()
    gen1=Radiobutton(register,text="Male",variable=var,value=1).pack()
    gen2=Radiobutton(register,text="Female",variable=var,value=2).pack()
    Label(register,text="Father's Name *").pack()
    father_entry=Entry(register,textvariable=father_name)
    father_entry.pack()
    Label(register,text="CGPA *").pack()
    cgpa_entry=Entry(register,textvariable=cgpa)
    cgpa_entry.pack()
    Label(register,text="Address *").pack()
    scroll=Entry(register,textvariable=txt)
    scroll.pack()
    Button(register,text="Register",width="10",height="1",bg="blue",fg="white",command=lambda:check(lb,var,txt)).pack()
    lb=Label(register,text="",fg="green")
    lb.pack()
    



#Login Details
def login():
    login=Toplevel(w)
    login.title("Login")
    login.geometry('300x300+200+200')
    login.iconbitmap(r'Student.ico')
    global username1
    global password1
    global username1_entry
    global pwd1_entry
    username1=StringVar()
    password1=StringVar()
    username1_label=Label(login,text="Username *")
    username1_label.pack()
    username1_entry=Entry(login,textvariable=username1)
    username1_entry.pack()
    pwd1_label=Label(login,text="Password *")
    pwd1_label.pack()
    pwd1_entry=Entry(login,textvariable=password1,show="*")
    pwd1_entry.pack()
    Button(login,text="Login",width="10",height="1",bg="blue",fg="white",command=lambda:[check_login(),login.destroy()]).pack()
    

#Main Screen For Login and Register
def main_screen():
    #Select the choice
    Label(text="Select your choice",bg="blue",width="300",height="3",font=("Calibri",12)).pack()
    Label(text="").pack()

    #Login Button
    Button(text="Login",height="3",width="30",font=("Calibri",12),command=login).pack()

    #Register Button
    Button(text="Register",height="3",width="30",font=("Calibri",12),command=register).pack()



w=Tk()
w.iconbitmap(r'chrome.ico')
w.title("Welcome to Student IMS")
w.geometry('300x300+300+300')
main_screen()
w.mainloop()
