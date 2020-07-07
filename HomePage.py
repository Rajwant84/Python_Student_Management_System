from tkinter import *
import sqlite3
import Admin
import Professor
import Student
import tkinter.messagebox

class HomePage:
    def __init__(self,master_window):
        # create DB
        connection_newDB = sqlite3.connect('SCHOOL_DATABASE.db')
        # create cursor
        cursor_newDB = connection_newDB.cursor()

        # create table for student database
        cursor_newDB.execute("""CREATE TABLE IF NOT EXISTS LOGIN_RECORDS (
                    LOGIN_TYPE text,
                    USER_NAME text,
                    USER_PASSWORD text,
                    PRIMARY KEY (USER_NAME,USER_PASSWORD)
                    )""")
        connection_newDB.commit()
        connection_newDB.close()

        self.master_window=master_window
        self.master_window.geometry('+400+200')
        self.master_window.title("HOME PAGE")
        self.master_window_Frame1=Frame(self.master_window)
        self.master_window_Frame2=Frame(self.master_window)
        self.master_window_Frame1.pack()
        self.master_window_Frame2.pack()

        self.master_label=Label(self.master_window_Frame1,text="LOGIN",font=("Times new Roman", 18))
        self.master_userType=''
        self.master_login_type=IntVar()
        self.master_login_type.set(1)
        self.master_login_choice_admin=Radiobutton(self.master_window_Frame1,text='Admin',variable=self.master_login_type,value=1)
        self.master_login_choice_prof=Radiobutton(self.master_window_Frame1,text='Professor',variable=self.master_login_type,value=2)
        self.master_login_choice_student=Radiobutton(self.master_window_Frame1,text='Student',variable=self.master_login_type,value=3)

        self.master_username_label=Label(self.master_window_Frame2,text="USERNAME")
        self.master_username=Entry(self.master_window_Frame2,width=20)
        self.master_password_label=Label(self.master_window_Frame2,text="PASSWORD")
        self.master_password=Entry(self.master_window_Frame2,width=20,show="*")

        self.master_login_button=Button(self.master_window_Frame2,text="LOGIN",command=self.login)
        self.master_signup_button=Button(self.master_window_Frame2,text="SIGNUP",command=self.signUP)

        self.master_label.grid(row=0,column=1,padx=20,pady=10)
        self.master_login_choice_admin.grid(row=1,column=0)
        self.master_login_choice_prof.grid(row=1,column=1)
        self.master_login_choice_student.grid(row=1,column=2)
        self.master_username_label.grid(row=2,column=0,padx=20,pady=10)
        self.master_username.grid(row=2,column=1,padx=20,pady=10)
        self.master_password_label.grid(row=3,column=0,padx=20)
        self.master_password.grid(row=3,column=1,padx=20)
        self.master_login_button.grid(row=4,column=0,padx=20, pady=20, ipadx=60)
        self.master_signup_button.grid(row=4,column=1,padx=20, pady=20, ipadx=60)

    def login( self ):
        if self.master_login_type.get()==1:
            self.master_userType='Admin'
        elif self.master_login_type.get()==2:
            self.master_userType='Professor'
        elif self.master_login_type.get()==3:
            self.master_userType='Student'

        connection_loginDB = sqlite3.connect('SCHOOL_DATABASE.db')
        cursor_loginDB = connection_loginDB.cursor()

        # create table for student database
        cursor_loginDB.execute("SELECT * FROM LOGIN_RECORDS")
        self.loginRecords=cursor_loginDB.fetchall()
        #print(self.loginRecords)
        connection_loginDB.commit()
        connection_loginDB.close()
        if len(self.master_username.get()) != 0 or len(self.master_password.get()) != 0:
            for self.login_test in self.loginRecords:
                if self.master_userType=='Admin' and self.login_test[0]==self.master_userType and self.login_test[1]==self.master_username.get() and self.login_test[2]==self.master_password.get():
                    Admin.Admin(Tk())
                    self.master_window.destroy()
                    break
                elif self.master_userType=='Professor' and self.login_test[0]==self.master_userType and self.login_test[1]==self.master_username.get() and self.login_test[2]==self.master_password.get():
                    Professor.Professor(Tk())
                    self.master_window.destroy()
                    break
                elif self.master_userType=='Student' and self.login_test[0]==self.master_userType and self.login_test[1]==self.master_username.get() and self.login_test[2]==self.master_password.get():
                    Student.Student(Tk())
                    self.master_window.destroy()
                    break
        else:
            tkinter.messagebox.showerror('ERROR','Empty Field NOT Allowed')

    def signUP( self ):
        if self.master_login_type.get()==1:
            self.master_userType='Admin'
        elif self.master_login_type.get()==2:
            self.master_userType='Professor'
        elif self.master_login_type.get()==3:
            self.master_userType='Student'

        connection_signupDB = sqlite3.connect('SCHOOL_DATABASE.db')
        # create cursor
        cursor_signupDB = connection_signupDB.cursor()

        if len(self.master_username.get()) != 0 or len(self.master_password.get()) != 0:
            try:
                cursor_signupDB.execute("INSERT INTO LOGIN_RECORDS VALUES (:LOGIN_TYPE,:USER_NAME,:USER_PASSWORD)",
                               {
                                   "LOGIN_TYPE": self.master_userType,
                                   "USER_NAME" : self.master_username.get(),
                                   "USER_PASSWORD" : self.master_password.get()
                               })
                tkinter.messagebox.showinfo('Successfull','Signup Successfull')
            except:
                tkinter.messagebox.showwarning('WARNING','User already exists')
        else:
            tkinter.messagebox.showerror('ERROR','Empty Field NOT Allowed')

        connection_signupDB.commit()
        connection_signupDB.close()
        self.master_username.delete(0,END)
        self.master_password.delete(0,END)


def main():
    root=Tk()
    Home_OBJ=HomePage(root)
    #Admin_OBJ=Admin.Admin(root)
    root.mainloop()

main()