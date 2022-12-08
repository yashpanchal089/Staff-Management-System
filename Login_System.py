from tkinter import *
#from PIL import ImageTk
from tkinter import messagebox

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1420x800+0+0')

    #====All Images==============
        #self.bg_icon=ImageTk.PhotoImage(file='C:\\Users\\Harsh\\Pictures\\Background.jpg')
        #self.user_icon=PhotoImage(file='C:\\Users\\Harsh\\Pictures\\icons8-user-account-64.png')
        #self.pass_icon = PhotoImage(file='C:\\Users\\Harsh\\Pictures\\icons8-password-64.png')
        #self.logo_icon = PhotoImage(file='C:\\Users\\Harsh\\Pictures\\icons8-iron-man-200.png')
    #=====Variabls=================
        self.name=StringVar()
        self.pass_=StringVar()
        #bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root, text='Login Page', font=('times new roman', 40, 'bold'), bg='lightpink',fg='black').place(x=0, y=0, relwidth=1)

        Login_Frame=Frame(self.root,bg='white')
        Login_Frame.place(x=400,y=150)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        lbluser=Label(Login_Frame,text='Username:',image=self.user_icon,compound=LEFT,font=('times new roman', 15, 'bold'),bg='white').grid(row=1,column=0,padx=20,pady=20)
        txtuser=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.name,font=('times new roman', 15, 'bold')).grid(row=1,column=1,padx=20,pady=20)
        lblpass = Label(Login_Frame, text='Password:', image=self.pass_icon, compound=LEFT,font=('times new roman', 15, 'bold'), bg='white').grid(row=2, column=0,padx=20,pady=20)
        txtpass = Entry(Login_Frame, bd=5, relief=GROOVE,textvariable=self.pass_,show='*' ,font=('times new roman', 15, 'bold')).grid(row=2, column=1,padx=20, pady=20)

        btn_log=Button(Login_Frame,text='Login',width=15,font=('times new roman', 15, 'bold'),bg='lightblue').grid(row=3,column=1,pady=10)


    def login(self):
        if self.name.get()=="" or self.passw.get()=="":
            messagebox.showerror(title='Error',message='All fields are required!!')
        elif self.name.get()=="Admin" or self.pass_.get()=="123456":
            messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
root = Tk()
obj = Login_System(root)
root.mainloop()
