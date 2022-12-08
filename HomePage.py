from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import os
#from PIL import ImageTk
import mysql.connector
"""mydb=mysql.connector.connect
    host='127.0.0.1',
    user='root',
    password='jsn',
    database='staffmangement')"""


class Salary:
    def __init__(self):
        self.window6 = Tk()
        self.window6.configure(background='black')
        self.window6.title('Salary Page')
        self.window6.configure(background='black')
        self.window6.geometry('900x550+330+165')
        self.window6.resizable(False,False)
        #====Initalizing Variables===================
        self.Name = StringVar()
        self.Email = StringVar()
        self.Mobile = StringVar()
        self.TotalSalary = StringVar()
        self.SalaryPN = None
        self.Bonus = StringVar()
        self.Deduction = StringVar()
        self.Loan = StringVar()

        Label(self.window6,text="Worker's Salary ", height=2, width=30, font=('arial',14,'bold'),bg='black', fg="white", bd=10).place(x=275,y=0)

        tkinter.Label(self.window6, text = "NAME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=60)
        tkinter.Label(self.window6, text = "EMAIL: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=100)
        tkinter.Label(self.window6, text = "MOBILE: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=140)
        tkinter.Label(self.window6, text = "TOTAL SALARY: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=180)
        tkinter.Label(self.window6, text = "SALARY \n PAID OR NOT: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=220)
        tkinter.Label(self.window6, text = "BONUS: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=276)
        tkinter.Label(self.window6, text = "DEDUCTION \n (PF,ESI,etc.): ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=315)
        tkinter.Label(self.window6, text = "LOAN ENTRY: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=372)

        #==Entry=================================
        self.E1=Entry(self.window6, bd=5, width=25,font=("bold", 10), textvariable=self.Name)
        self.E1.place(x=450,y=60)
        self.E2=Entry(self.window6, bd=5, width=25,font=("bold", 10), textvariable=self.Mobile)
        self.E2.place(x=450,y=100)
        self.E3=Entry(self.window6, bd=5, width=25,font=("bold", 10), textvariable=self.Email)
        self.E3.place(x=450,y=140)
        self.E4=Entry(self.window6, bd=5, width=25,font=("bold", 10), textvariable=self.TotalSalary)
        self.E4.place(x=450,y=180)
        self.E5=Entry(self.window6, bd=5, width=25,font=("bold", 10), textvariable=self.Bonus)
        self.E5.place(x=450,y=274)
        self.E6=Entry(self.window6, bd=5, width=25,font=("bold", 10), textvariable=self.Deduction)
        self.E6.place(x=450,y=321)
        self.E7=Entry(self.window6, bd=5, width=25,font=("bold", 10), textvariable=self.Loan)
        self.E7.place(x=450,y=370)


        self.R1 = Button(self.window6, text="Paid",  height=1, width=8, font=('arial',10,'bold'),bd=5, bg="lightblue",command = self.SetSalaryPaid)
        self.R1.place(x=450,y=225)
        self.R2 = Button(self.window6, text="Not", height=1, width=8, font=('arial',10,'bold'), bd=5, bg="lightblue",command = self.SetSalaryNot)
        self.R2.place(x=520,y=225)

        B1 = Button(self.window6, text="SUBMIT", height=2, width=8,font=('arial',10,'bold'), bd=5, bg='lightgreen', fg='black', command=self.Database).place(x=370,y=425)
        B2 = Button(self.window6, text="BACK ", height=2, width=5, font=('arial',10,'bold'), bd=5, bg='lightgreen', fg='black',command=self.window6.destroy).place(x=530,y=425)

    def SetSalaryPaid(self):
        self.R1.config(bg = "lightgreen")
        self.R2.config(bg = "white")
        self.SalaryPN = "Paid"

    def SetSalaryNot(self):
        self.R1.config(bg = "white")
        self.R2.config(bg = "lightgreen")
        self.SalaryPN = "Not"


        #=========Database=====================================================

    """def Database(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='jsn',database='staffmangement')
        name = str(self.E1.get())
        email = str(self.E2.get())
        mobile = str(self.E3.get())
        totalsalary = str(self.E4.get())
        salarypn = str(self.SalaryPN)
        bonus = str(self.E5.get())
        deduction = str(self.E6.get())
        loan = str(self.E7.get())
        d=conn.cursor()
        #d.execute('create table salary(name varchar(50), mobile_no varchar(15), comingtime varchar(15), leavingtime varchar(15), lunch_provided varchar(15), overtime varchar(15));')
        test3 = "INSERT INTO salary(name,email,mobile,totalsalary,salarypn,bonus,deduction,loan) VALUES('"+name+"','"+email+"','"+mobile+"','"+totalsalary+"','"+salarypn+"','"+bonus+"','"+deduction+"','"+loan+"')"
        #print(test3)
        d.execute(test3)
        conn.commit()
        self.window6.destroy()
        tkinter.messagebox.showinfo(title='Successfully', message='Your Detalis Successfully Added')"""

    self.window6.mainloop()


class StaffRegistration:
    def __init__(self):
        self.window = Tk()
        self.window.title('STAFF REGISTRATION')
        self.window.configure(background='black')
        self.window.geometry('900x650+300+135')
        self.window.resizable(False,False)
    #====Initalizing Variables===================
        self.Name = StringVar()#label1
        self.Email = StringVar()#label2
        self.Mobile = StringVar()#label3
        self.Address = StringVar()#label4
        self.Dob = StringVar()#label5
        self.Age= StringVar()#label6
        self.Gender = None
        self.Salary_type = StringVar()#label8
        self.Salary = StringVar()#label9
        self.SalaryCycle = StringVar()#label10
        
        self.Salary_Box = ["MONTHLY", "PER HOUR BASIS","DAILY","WORK BASIS","WEEKLY"]
        self.Salary_Cycle = ["1 to 1 of every month", "2 to 2 of every month","3 to 3 of every month","4 to 4 of every month","5 to 5 of every month","6 to 6 of every month",
                                      "7 to 7 of every month", "8 to 8 of every month", "9 to 9 of every month", "10 to 10 of every month", "11 to 11 of every month", "12 to 12 of every month",
                                      "13 to 13 of every month", "14 to 14 of every month", "15 to 15 of every month", "16 to 16 of every month", "17 to 17 of every month", "18 to 18 of every month",
                                      "19 to 19 of every month", "20 to 20 of every month", "21 to 21 of every month", "22 to 22 of every month", "23 to 23 of every month", "24 to 24 of every month",
                                      "25 to 25 of every month", "26 to 26 of every month", "27 to 27 of every month", "28 to 28 of every month", "29 to 29 of every month", "30 to 30 of every month",
                                      "31 to 31 of every month"]

        self.GenderList = ["Male", "Female","Other"]
        self.AgeList = list(range(1,100))

    
        Label(self.window,text="+ADD STAFF ", height=2, width=30, font=('arial',14,'bold'),bg='black', fg="white", bd=10).place(x=275,y=0)


        tkinter.Label(self.window, text = "NAME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=60)
        tkinter.Label(self.window, text = "EMAIL: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=100)
        tkinter.Label(self.window, text = "MOBILE: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=140)
        tkinter.Label(self.window, text = "ADDRESS: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=180)
        tkinter.Label(self.window, text = "DOB(DD-MM-YYY): ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=300)
        tkinter.Label(self.window, text = "AGE: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=340)
        tkinter.Label(self.window, text = "GENDER: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=380)
        tkinter.Label(self.window, text = "SALARY TYPE: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=420)
        tkinter.Label(self.window, text = "SALARY: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=460)
        tkinter.Label(self.window, text = "SALARY CYCLE: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=300,y=500)


    #==Entry=================================
        self.E1=Entry(self.window, bd=5, width=25,font=("bold", 10))
        self.E1.place(x=450,y=60)
        self.E2=Entry(self.window, bd=5, width=25,font=("bold", 10))
        self.E2.place(x=450, y=100)
        self.E3=Entry(self.window, bd=5, width=25,font=("bold", 10))
        self.E3.place(x=450,y=140)
        self.E4=Entry(self.window, bd=5, width=25,font=("bold", 10))
        self.E4.place(x=450,y=180,height=100)
        self.E5=Entry(self.window, bd=5, width=25,font=("bold", 10))
        self.E5.place(x=450,y=300)
        self.E6=Entry(self.window, bd=5, width=25,font=("bold", 10))
        self.E6.place(x=450,y=458)
        
        self.ageBox = tkinter.ttk.Combobox(self.window, values = self.AgeList, width = 5,font=("bold", 12))
        self.ageBox.place(x=450,y=340)
        self.salaryBox = tkinter.ttk.Combobox(self.window, values = self.Salary_Box, width = 20,font=("bold", 10))
        self.salaryBox.place(x=450,y=420)
        self.salaryCycle = tkinter.ttk.Combobox(self.window, values = self.Salary_Cycle, width = 20,font=("bold", 10))
        self.salaryCycle.place(x=450,y=500)

        self.R1 = Button(self.window, text="Male ", height=1, width=8,font=('arial',10,'bold'), bd=5, bg='white', fg='black', command = self.SetGenderMale)
        self.R1.place(x=450,y=380)
        self.R2 = Button(self.window, text="Female ", height=1, width=8,font=('arial',10,'bold'), bd=5, bg='white', fg='black', command = self.SetGenderFemale)
        self.R2.place(x=520,y=380)
        self.R3 = Button(self.window, text="Other ", height=1, width=8,font=('arial',10,'bold'), bd=5, bg='white', fg='black', command = self.SetGenderOther)
        self.R3.place(x=590,y=380)
        
        B1 = Button(self.window, text="SUBMIT ", height=2, width=8,font=('arial',10,'bold'), bd=5, bg='lightgreen', fg='black',command=self.Database).place(x=325,y=570)
        B2 = Button(self.window, text="BACK ", height=2, width=5, font=('arial',10,'bold'), bd=5, bg='lightgreen', fg='black',command=self.window.destroy).place(x=525,y=570)

    def SetGenderMale(self):
        self.R1.config(bg = "lightgreen")
        self.R2.config(bg = "white")
        self.R3.config(bg = "white")
        self.Gender = "Male"

    def SetGenderFemale(self):
        self.R1.config(bg = "white")
        self.R2.config(bg = "lightgreen")
        self.R3.config(bg = "white")
        self.Gender = "Female"

    def SetGenderOther(self):
        self.R1.config(bg = "white")
        self.R2.config(bg = "white")
        self.R3.config(bg = "lightgreen")
        self.Gender = "Other"
        
        #========Database========================================
        
    """def Database(self):
       conn=mysql.connector.connect(host='127.0.0.1',user='root',password='jsn',database='staffmangement')
       name=str(self.E1.get())#label1
       email=str(self.E2.get())#label2
       mobile=str(self.E3.get())#label3
       address=str(self.E4.get())#label4
       dob=str(self.E5.get())#label5
       age=str(self.ageBox.get())#label6
       gender=str(self.Gender)#label7
       salarytype=str(self.salaryBox.get())#label8
       salary=str(self.E6.get())#label9
       salarycycle=str(self.salaryCycle.get())#label10
       d=conn.cursor()
       #d.execute('create table addnewstaff(name varchar(50), email varchar(50), mobile varchar(10), address varchar(100), dob varchar(10), age varchar(5), gender varchar(10), salary_type varchar(25), salary varchar(10), salary_cycle varchar(30));')
       test = "INSERT INTO addnewstaff(name,email,mobile,address,dob,age,gender,salary_type,salary,salary_cycle) VALUES('"+name+"','"+email+"','"+mobile+"','"+address+"','"+dob+"','"+age+"','"+gender+"','"+salarytype+"','"+salary+"','"+salarycycle+"')"
       d.execute(test)
       conn.commit()
       self.window.destroy()
       tkinter.messagebox.showinfo(title='Successfully', message='Your Worker Number: '+str(random.randint(10000, 99999)))"""
       

class TMP:
    def __init__(self):
        self.window3 = Tk()
        self.window3.title('TEMPORARY WORKER ATTENDANCE')
        self.window3.configure(background='black')
        self.window3.geometry('735x390+400+190')
        self.window3.resizable(False,False)
        #====Initalizing Variables===================
        self.Name = StringVar()
        self.Mobile = StringVar()
        self.Lunch = None
        self.Comingtime = ["1.00", "2.00","3.00","4.00","5.00","6.00","7.00","8.00","9.00","10.00","11.00","12.00"]
        self.Overtime = ["1.00hr", "2.00hr","3.00hr","4.00hr","5.00hr","6.00hr","7.00hr","8.00hr","9.00hr","10.00hr","11.00hr","12.00hr"]
        self.Leavtime=["1.00", "2.00","3.00","4.00","5.00","6.00","7.00","8.00","9.00","10.00","11.00","12.00"]

        tkinter.Label(self.window3, text = "NAME:",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=60)
        tkinter.Label(self.window3, text = "MOBILE NO: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=380,y=60)
        tkinter.Label(self.window3, text = "COMMING TIME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=100)
        tkinter.Label(self.window3, text = "LUNCH PROVIDED: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=140)
        tkinter.Label(self.window3, text = "OVERTIME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=180)
        tkinter.Label(self.window3, text = "LEAVING TIME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=380,y=100)

        #======Entry=====================================

        self.E1=Entry(self.window3, bd=5, width=25,font=("bold", 10), textvariable=self.Name)
        self.E1.place(x=150,y=60)
        self.E2=Entry(self.window3, bd=5, width=25,font=("bold", 10), textvariable=self.Mobile)
        self.E2.place(x=510,y=60)
        
        self.Com_Time= tkinter.ttk.Combobox(self.window3, values = self.Comingtime, width = 24,font=("bold", 10))
        self.Com_Time.place(x=150,y=100)
        self.Over_Time = tkinter.ttk.Combobox(self.window3, values = self.Overtime, width = 24,font=("bold", 10))
        self.Over_Time.place(x=150,y=180)
        self.Leav_Time = tkinter.ttk.Combobox(self.window3, values = self.Leavtime, width = 24,font=("bold", 10))
        self.Leav_Time.place(x=510,y=100)

        self.R1 = Button(self.window3, text="Yes ", height=1, width=8,font=('arial',10,'bold'), bd=5, bg='white', fg='black', command = self.SetLunchYes)
        self.R1.place(x=180,y=140)
        self.R2 = Button(self.window3, text="No ", height=1, width=8,font=('arial',10,'bold'), bd=5, bg='white', fg='black', command = self.SetLunchNo)
        self.R2.place(x=250,y=140)

        b1 = Button(self.window3, text="SUBMIT", height=2, width=10, font=('arial',10,'bold'),command=self.Database, bd=5, bg='lightblue', fg='black').place(x=150,y=220)
        b2 = Button(self.window3, text="BACK ", height=2, width=10, font=('arial',10,'bold'), bd=5, bg='lightblue', fg='black',command=self.window3.destroy).place(x=260,y=220)
        b3 = Button(self.window3, text="STAFF\nREGISTRATION ", height=2, width=15,command=StaffRegistration, font=('arial',10,'bold'), bd=5, bg='lightgreen', fg='black').place(x=370,y=220)


    def SetLunchYes(self):
        self.R1.config(bg = "lightgreen")
        self.R2.config(bg = "white")
        self.Lunch = "Yes"

    def SetLunchNo(self):
        self.R1.config(bg = "white")
        self.R2.config(bg = "lightgreen")
        self.Lunch = "No"
        
        
        #=======Database================================


    """def Database(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='jsn',database='staffmangement')
        name=str(self.E1.get())
        mobile_no=str(self.E2.get())
        lunch_provided=str(self.Lunch)
        comingtime=str(self.Com_Time.get())
        overtime=str(self.Over_Time.get())
        leavingtime=str(self.Leav_Time.get())
        d=conn.cursor()
        #d.execute('create table twa(name varchar(50), mobile_no varchar(15), comingtime varchar(15), leavingtime varchar(15), lunch_provided varchar(15), overtime varchar(15));')
        test2 = "INSERT INTO twa(name,mobile_no,comingtime,leavingtime,lunch_provided,overtime) VALUES('"+name+"','"+mobile_no+"','"+comingtime+"','"+leavingtime+"','"+lunch_provided+"','"+overtime+"')"
        #print(test)
        d.execute(test2)
        conn.commit()
        self.window3.destroy()
        tkinter.messagebox.showinfo(title='Successfully', message='Your Detalis Successfully Added')"""

        self.window3.mainloop()

class PWA:
    def __init__(self):
        self.window4 = Tk()
        self.window4.title('PERMENT WORKER ATTENDANCE')
        self.window4.configure(background='black')
        self.window4.geometry('735x390+400+190')
        self.window4.resizable(False,False)
        #====Initalizing Variables=====================
        self.Name = StringVar()
        self.Comingtime = StringVar()
        self.Workdetail = StringVar()
        self.Overtime = StringVar()
        self.Mobileno = IntVar()
        self.Leavingime = StringVar()
        self.Date = StringVar()
        self.Latefine = StringVar()
        self.Paidholiday = StringVar()
        
        self.ComingTime = ["1.00", "2.00","3.00","4.00","5.00","6.00","7.00","8.00","9.00","10.00","11.00","12.00"]#Comingime
        self.OverTime = ["1.00hr", "2.00hr","3.00hr","4.00hr","5.00hr","6.00hr","7.00hr","8.00hr","9.00hr","10.00hr","11.00hr","12.00hr"]#Overtime
        self.LeavingTime=["1.00", "2.00","3.00","4.00","5.00","6.00","7.00","8.00","9.00","10.00","11.00","12.00"]#LeavingTime


        tkinter.Label(self.window4, text = "NAME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=60)
        tkinter.Label(self.window4, text = "COMING TIME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=100)
        tkinter.Label(self.window4, text = "WORK DETAIL: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=140)
        tkinter.Label(self.window4, text = "OVERTIME ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=20,y=245)
        tkinter.Label(self.window4, text = "MOBILE NO: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=380,y=60)
        tkinter.Label(self.window4, text = "LEAVING TIME: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=380,y=100)
        tkinter.Label(self.window4, text = "DATE: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=380,y=140)
        tkinter.Label(self.window4, text = "LATE FINE: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=380,y=180)
        tkinter.Label(self.window4, text = "PAID HOLIDAY: ",  width = 15,font=('arial', 10,'bold'),bg="lightblue").place(x=380,y=220)

        #==========Entry=======================

        self.E1=Entry(self.window4, bd=5, width=25,font=("bold", 10))#Name
        self.E1.place(x=150,y=60)
        self.E2=Entry(self.window4, bd=5, width=25,font=("bold", 10))#Mobile
        self.E2.place(x=510,y=60)
        self.E3=Entry(self.window4, bd=5, width=25,font=("bold", 10))#Date
        self.E3.place(x=510,y=140)
        self.E4=Entry(self.window4, width=25, font=("bold", 10),bd=5)#Workdetail
        self.E4.place(x=150,y=140, height = 100)
        self.E5=Entry(self.window4, width=25, font=("bold", 10),bd=5)#Latefine
        self.E5.place(x=510,y=180)        
        self.E6=Entry(self.window4, width=25, font=("bold", 10),bd=5)#Paidholiday
        self.E6.place(x=510,y=220)
        
        self.Comingtime = tkinter.ttk.Combobox(self.window4, values = self.ComingTime, width = 23, font=("bold", 10))#Comingtime
        self.Comingtime.place(x=153,y=100)
        self.Overtime = tkinter.ttk.Combobox(self.window4, values = self.OverTime, width = 23,font=("bold", 10))#Overtime
        self.Overtime.place(x=153,y=245)
        self.Leavingtime = tkinter.ttk.Combobox(self.window4, values = self.LeavingTime, width = 23,font=("bold", 10))#Leavingtime
        self.Leavingtime.place(x=513,y=100)

        b1 = Button(self.window4, text="SUBMIT",command=self.Database, height=2, width=10, font=('arial',10,'bold'), bd=5, bg='lightblue', fg='black').place(x=150,y=280)
        b2 = Button(self.window4, text="BACK ", height=2, width=10, font=('arial',10,'bold'), bd=5, bg='lightyellow', fg='black',command=self.window4.destroy).place(x=260,y=280)
        b3 = Button(self.window4, text="STAFF\nREGISTRATION ", height=2, width=15,command=StaffRegistration, font=('arial',10,'bold'), bd=5, bg='lightgreen', fg='black').place(x=370,y=280)

        #=============Database======================
       
    """def Database(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='jsn',database='staffmangement')
        name=str(self.E1.get())
        mobile=str(self.E2.get())
        date=str(self.E3.get())
        workdetail=str(self.E4.get())
        latefine=str(self.E5.get())
        paidholiday=str(self.E6.get())
        comingtime=str(self.Comingtime.get())
        overtime=str(self.Overtime.get())
        leavingtime=str(self.Leavingtime.get())
        d=conn.cursor()
        #d.execute('create table pwa(name varchar(50), mobile varchar(15), date varchar(15), work_detail varchar(15), latefine varchar(200), paidholiday varchar(15), comingtime varchar(15), overtime varchar(15), leavingtime varchar(15));')
        test1 = "INSERT INTO pwa(name,mobile,comingtime,leavingtime,work_detail,date,latefine,paidholiday,overtime) VALUES('"+name+"','"+mobile+"','"+comingtime+"','"+leavingtime+"','"+workdetail+"','"+date+"','"+latefine+"','"+paidholiday+"','"+overtime+"')"
        #print(test1)
        d.execute(test1)
        conn.commit()
        self.window4.destroy()
        tkinter.messagebox.showinfo(title='Successfully', message='Your Detalis Successfully Added')"""


        self.window4.mainloop()



class Attendance:
    def __init__(self):
        self.window2 = Tk()
        self.window2.title('ATTENDANCE')
        self.window2.configure(background='grey')
        self.window2.geometry('1530x790+0+0')
        self.window2.resizable(False,False)
        Label(self.window2,text="WORKER ATTENDANCE PAGE", height=2, width=30, font=('arial',25,'bold'),bg='black', fg="white", bd=10).place(x=460,y=0)

        b1 = Button(self.window2, text="PERMENT\nWORKER", height=5, width=10,command=PWA, font=('arial',15,'bold'), bd=10, bg='lightblue', fg='black').place(x=600,y=250)
        b2 = Button(self.window2, text="TEMPORARY\nWORKER", height=5, width=10,command=TMP, font=('arial',15,'bold'), bd=10, bg='lightblue', fg='black').place(x=780,y=250)
        b3 = Button(self.window2, text="BACK ", height=2, width=20, font=('arial',10,'bold'), bd=5, bg='lightyellow', fg='black',command=self.window2.destroy).place(x=680,y=450)


        self.window2.mainloop()

class About:
    def __init__(self):
        self.window1 = Tk()
        self.window1.title('ABOUT US & CONTACT US')
        self.window1.configure(background='grey')
        self.window1.geometry('800x500+380+170')
        self.window1.resizable(False,False)
        tkinter.Label(self.window1, text = "YASH's STAFF MANAGEMENT",  width = 50,height=2,font=('arial', 12,'bold'),bg="black", fg="white").place(x=150,y=0)
        tkinter.Label(self.window1, text = "Created by: Yash Panchal ",  width = 45, height=2, font=('arial', 10,'bold'),bg="black", fg="white").place(x=220,y=40)
        Frame1=Frame(self.window1,bg='white')
        Frame1.place(x=235,y=165)
        lbluser=Label(Frame1,text='Yash Panchal\nContact Number: 9004168049\nEmail: panchalyash089@gmail.com',font=('times new roman', 15, 'bold'),bg='white').grid(row=1,column=0,padx=20,pady=20)


        b1 = Button(self.window1, text="BACK ", height=2, width=5, font=('arial',10,'bold'), bd=5, bg='lightyellow', fg='black',command=self.window1.destroy).place(x=375,y=350)

        self.window1.mainloop
        
class Registration:
    def __init__(self):
       root = self.root = Tk()
       root.title('STAFF REGISTRATION')
       root.geometry('1530x790+0+0')
       root.resizable(False,False)
       root.configure(background='lightblue')
       Label(root,text="STAFF REGISTRATION PAGE", height=2, width=30, font=('arial',25,'bold'),bg='black', fg="white", bd=10).place(x=460,y=0)
       b1 = Button(root, text="+ADD \nSTAFF ", height=2, width=30,command=StaffRegistration, font=('arial',15,'bold'), bd=5, bg='black', fg='white').place(x=600,y=250)
       b2 = Button(root, text="BACK ", height=2, width=5, font=('arial',10,'bold'), bd=5, bg='lightyellow', fg='black',command=root.destroy).place(x=763,y=350)

       root.mainloop()

class HomePage:
    def __init__(self):
        top = Tk()
        top.geometry('1530x790+0+0')
        top.resizable(False,False)
        top.title('STAFF MANAGEMENT SYSTEM')
        top.configure(background='gray')
        #b2_icon=ImageTk.PhotoImage(file='G:\\Project\\icons8-car-100.png')
        #b1_icon=PhotoImage(file='G:\\Project\\icons8-heart-with-pulse-100.png')


    #=====Label=================
        Label(top,text="Staff Management System", height=2, width=50, font=('arial',30,'bold'),bg='black', fg="white", bd=10).place(x=180,y=0)
    #===Buttons================
        b2 = Button(top, text="Registration",height=5, width=10, font=('arial',10,'bold'), bd=10, bg='lightblue', fg='black',command=Registration).place(x=490,y=320)
        b3 = Button(top, text="Attendance", height=5, width=10, command=Attendance, font=('arial',10,'bold'),bd=10, bg='lightblue', fg='black').place(x=610,y=320)
        b4 = Button(top, text="Salary", height=5, command=Salary, width=10,font=('arial',10,'bold'), bd=10, bg='lightblue', fg='black').place(x=730,y=320)
        b5 = Button(top, text="Contact Us &\nAbout Us", height=5, width=10, font=('arial',10,'bold'),command=About, bd=10, bg='lightblue', fg='black').place(x=853,y=320)
        b6 = Button(top, text="Exit", height=5, width=10,font=('arial',10,'bold'), bd=10, bg='lightblue', fg='black',command=top.destroy).place(x=975,y=320)


class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title('Login')
        self.root.resizable(False,False)
        self.root.geometry('1530x790+0+0')

    #====All Images==============
        self.bg_icon=ImageTk.PhotoImage(file='G:\\Project 1\\Project\\Background4.jpg')
        self.user_icon=PhotoImage(file='G:\\Project 1\\Project\\icons8-user-account-64.png')
        self.pass_icon = PhotoImage(file='G:\\Project 1\\Project\\icons8-password-64.png')
        self.logo_icon = PhotoImage(file='G:\\Project 1\\Project\\icons8-iron-man-200.png')
    #=====Variabls=================
        self.name=StringVar()
        self.pass_=StringVar()
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root, text='Login Page',font=('times new rom0an', 40, 'bold'), bg='black',fg='white').place(x=0, y=0, relwidth=1)

        Login_Frame=Frame(self.root,bg='white')
        Login_Frame.place(x=550,y=125)

        logolbl=Label(Login_Frame,bd=0).grid(row=0,columnspan=2,pady=20)
        lbluser=Label(Login_Frame,text='Username:',compound=LEFT,image=self.user_icon,font=('times new roman', 15, 'bold'),bg='white').grid(row=1,column=0,padx=20,pady=20)
        txtuser=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.name,font=('times new roman', 15, 'bold')).grid(row=1,column=1,padx=20,pady=20)
        lblpass = Label(Login_Frame, text='Password:', compound=LEFT,image=self.pass_icon,font=('times new roman', 15, 'bold'), bg='white').grid(row=2, column=0,padx=20,pady=20)
        txtpass = Entry(Login_Frame, bd=5, relief=GROOVE,textvariable=self.pass_,show='*', font=('times new roman', 15, 'bold')).grid(row=2, column=1,padx=20, pady=20)

        btn_log=Button(Login_Frame,text='Login',width=15,font=('times new roman', 15, 'bold'),bg='lightblue',command=self.login,).grid(row=3,column=1,pady=10)


    def login(self):
        if self.name.get()=="" or self.pass_.get()=="":
           tkinter.messagebox.showerror(title='Error',message='All fields are required!!')
        elif self.name.get()=="a" and self.pass_.get()=="a":
           tkinter.messagebox.showinfo(title='Successfully', message='Welcome '+ self.name.get())
           self.root.destroy()
           HomePage()
        else:
            tkinter.messagebox.showwarning(title='Error', message='invalid credentials !!')



root = Tk()
obj = Login_System(root)
root.mainloop()

#homepage = HomePage()
#if __name__=="__main__":
  #  a=StaffRegistration()
    #a.Database()
    #print("Done")
