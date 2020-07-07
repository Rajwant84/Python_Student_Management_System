from tkinter import *
import sqlite3
import tkinter.messagebox

class Admin:
    def __init__(self,admin_window):
        # create DB
        connection_newDB = sqlite3.connect('SCHOOL_DATABASE.db')
        #create cursor
        cursor_newDB = connection_newDB.cursor()

        # create table for student database
        cursor_newDB.execute("""CREATE TABLE IF NOT EXISTS STUDENT_RECORDS (
            STUDENT_NUMBER varchar(20),
            STUDENT_NAME text,
            COURSE_NUMBER varchar(20),
            COURSE_NAME text,
            PROFESSOR_NAME text,
            GRADE int,
            PRIMARY KEY (STUDENT_NUMBER)
            )""")
        connection_newDB.commit()
        connection_newDB.close()

        self.admin_window=admin_window
        self.admin_window.geometry("450x600+350+50")
        self.admin_window.title("ADMINISTRATOR")

        self.admin_window_Frame1=Frame(self.admin_window)
        self.admin_window_Frame2=Frame(self.admin_window)
        self.admin_window_Frame1.pack()
        self.admin_window_Frame2.pack()
        self.Frame1_LabelHead=Label(self.admin_window_Frame1,text="ADMINISTRATOR CONSOLE",font=("Times new Roman", 18))
        self.Frame1_LabelHead.pack()

        self.admin_student_number_label=Label(self.admin_window_Frame2,text="STUDENT NUMBER")
        self.admin_student_number=Entry(self.admin_window_Frame2,width=30)
        self.admin_student_name_label=Label(self.admin_window_Frame2,text="STUDENT NAME")
        self.admin_student_name=Entry(self.admin_window_Frame2,width=30)
        self.admin_course_number_label=Label(self.admin_window_Frame2,text="COURSE NUMBER")
        self.admin_course_number=Entry(self.admin_window_Frame2,width=30)
        self.admin_course_name_label=Label(self.admin_window_Frame2,text="COURSE NAME")
        self.admin_course_name=Entry(self.admin_window_Frame2,width=30)
        self.admin_professor_name_label=Label(self.admin_window_Frame2,text="PROFESSOR NAME")
        self.admin_professor_name=Entry(self.admin_window_Frame2,width=30)
        self.admin_grade_label=Label(self.admin_window_Frame2,text="GRADES")
        self.admin_grade=Entry(self.admin_window_Frame2,width=30)

        self.admin_insert_button=Button(self.admin_window_Frame2,text="ADD A RECORD",command=self.newRecord)
        self.admin_showRecord_button=Button(self.admin_window_Frame2,text="SHOW STUDENT RECORD",command=self.showRecord)

        self.admin_student_record_label=Label(self.admin_window_Frame2,text="REFERENCE ID")
        self.admin_student_record=Entry(self.admin_window_Frame2,width=30)
        self.admin_student_record.insert(0,0)

        self.admin_student_record_edit_button=Button(self.admin_window_Frame2,text="EDIT STUDENT RECORD",command=self.editRecord)
        self.admin_student_record_delete_button=Button(self.admin_window_Frame2,text="DELETE STUDENT RECORD",command=self.deleteRecord)
        #self.admin_newLogin_button = Button(self.admin_window_Frame2, text="CREATE NEW LOGIN",command=self.newLogin)
        self.admin_exit_button = Button(self.admin_window_Frame2, text="LOG OUT", command=self.admin_window.destroy)

        self.admin_student_number_label.grid(row=0,column=0)
        self.admin_student_number.grid(row=0,column=1,padx=20)
        self.admin_student_name_label.grid(row=1,column=0)
        self.admin_student_name.grid(row=1,column=1,padx=20)
        self.admin_course_number_label.grid(row=2,column=0)
        self.admin_course_number.grid(row=2,column=1,padx=20)
        self.admin_course_name_label.grid(row=3,column=0)
        self.admin_course_name.grid(row=3,column=1,padx=20)
        self.admin_professor_name_label.grid(row=4,column=0)
        self.admin_professor_name.grid(row=4,column=1,padx=20)
        self.admin_grade_label.grid(row=5,column=0)
        self.admin_grade.grid(row=5,column=1,padx=20)
        self.admin_insert_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
        self.admin_showRecord_button.grid(row=7, column=0, columnspan=2, padx=10, ipadx=120)
        self.admin_student_record_label.grid(row=8,column=0, pady=10)
        self.admin_student_record.grid(row=8,column=1, pady=10)
        self.admin_student_record_edit_button.grid(row=9, column=0, columnspan=2, ipadx=125)
        self.admin_student_record_delete_button.grid(row=10, column=0, columnspan=2, pady=10, ipadx=118)
        #self.admin_newLogin_button.grid(row=11, column=0, columnspan=2, ipadx=135)
        self.admin_exit_button.grid(row=12, column=0, columnspan=2,pady=10, ipadx=165)

    def newRecord( self ):
        if (len(self.admin_student_number.get()) != 0 or len(self.admin_student_name.get())) !=0 and len(self.admin_grade.get()) != 0:
            if int(self.admin_grade.get()) >= 0 and int(self.admin_grade.get()) <= 100:
                con_insert = sqlite3.connect('SCHOOL_DATABASE.db')
                cursor_insert = con_insert.cursor()
                cursor_insert.execute(
                    "INSERT INTO STUDENT_RECORDS VALUES (:stu_id, :stu_name, :course_id, :course_name, :prof_name, :grade)",
                    {
                        'stu_id': self.admin_student_number.get(),
                        'stu_name': self.admin_student_name.get(),
                        'course_id': self.admin_course_number.get(),
                        'course_name': self.admin_course_name.get(),
                        'prof_name': self.admin_professor_name.get(),
                        'grade': self.admin_grade.get()
                    })
                con_insert.commit()
                con_insert.close()

                self.admin_student_number.delete(0, END)
                self.admin_student_name.delete(0, END)
                self.admin_course_number.delete(0, END)
                self.admin_course_name.delete(0, END)
                self.admin_professor_name.delete(0, END)
                self.admin_grade.delete(0, END)
            else:
                print("Invalid Grade, OUT OF LIMIT")
        else:
            print("Empty fields not allowed")

    def showRecord( self ):
        # Create a database or connect to one
        conn_showRecord = sqlite3.connect('SCHOOL_DATABASE.db')

        cursor_showRecord = conn_showRecord.cursor()

        cursor_showRecord.execute("SELECT *, oid FROM STUDENT_RECORDS")
        records = cursor_showRecord.fetchall()

        print_records = ''
        headingLabel="REF. ID"+ "\t" + "STUDENT NUMBER"+ "\t" + "STUDENT NAME"+ "\t" + "GRADES"
        for record in records:
            print_records += str(record[6])+ "\t\t" + str(record[0])+ "  \t\t  " + str(record[1]) + "  \t  " + str(record[5]) + "\n"

        heading_label = Label(self.admin_window_Frame2, text=headingLabel)
        heading_label.grid(row=13, column=0, columnspan=3)

        query_label = Label(self.admin_window_Frame2, text=print_records)
        query_label.grid(row=14, column=0, columnspan=3)

        # Commit Changes
        conn_showRecord.commit()

        # Close Connection
        conn_showRecord.close()

    def editRecord( self ):
        if len(self.admin_student_record.get()) != 0:
            self.admin_recordEditor=Tk()
            self.admin_recordEditor.title("RECORD EDITOR")
            self.admin_recordEditor.geometry("400x300")
            conn_editRecord = sqlite3.connect('SCHOOL_DATABASE.db')

            cursor_editRecord = conn_editRecord.cursor()
            cursor_editRecord.execute("SELECT * FROM STUDENT_RECORDS WHERE OID="+self.admin_student_record.get())
            self.allStudents=cursor_editRecord.fetchall()

            self.admin_editor_head_label=Label(self.admin_recordEditor,text="STUDENT RECORD EDITOR",font=("Times New Roman",18))
            self.admin_student_number_editor_label=Label(self.admin_recordEditor,text="STUDENT NUMBER")
            self.admin_student_number_editor=Entry(self.admin_recordEditor,width=30)
            self.admin_student_name_editor_label=Label(self.admin_recordEditor,text="STUDENT NAME")
            self.admin_student_name_editor=Entry(self.admin_recordEditor,width=30)
            self.admin_course_number_editor_label=Label(self.admin_recordEditor,text="COURSE NUMBER")
            self.admin_course_number_editor=Entry(self.admin_recordEditor,width=30)
            self.admin_course_name_editor_label=Label(self.admin_recordEditor,text="COURSE NAME")
            self.admin_course_name_editor=Entry(self.admin_recordEditor,width=30)
            self.admin_professor_name_editor_label=Label(self.admin_recordEditor,text="PROFESSOR NAME")
            self.admin_professor_name_editor=Entry(self.admin_recordEditor,width=30)
            self.admin_grade_editor_label=Label(self.admin_recordEditor,text="GRADES")
            self.admin_grade_editor=Entry(self.admin_recordEditor,width=30)

            self.admin_editor_head_label.grid(row=0,column=0,padx=20,pady=20,columnspan=2)
            self.admin_student_number_editor_label.grid(row=1,column=0)
            self.admin_student_number_editor.grid(row=1,column=1)
            self.admin_student_name_editor_label.grid(row=2,column=0)
            self.admin_student_name_editor.grid(row=2,column=1)
            self.admin_course_number_editor_label.grid(row=3,column=0)
            self.admin_course_number_editor.grid(row=3,column=1)
            self.admin_course_name_editor_label.grid(row=4,column=0)
            self.admin_course_name_editor.grid(row=4,column=1)
            self.admin_professor_name_editor_label.grid(row=5,column=0)
            self.admin_professor_name_editor.grid(row=5,column=1)
            self.admin_grade_editor_label.grid(row=6,column=0)
            self.admin_grade_editor.grid(row=6,column=1)

            for self.eachStudent in self.allStudents:
                self.admin_student_number_editor.insert(0,self.eachStudent[0])
                self.admin_student_name_editor.insert(0,self.eachStudent[1])
                self.admin_course_number_editor.insert(0,self.eachStudent[2])
                self.admin_course_name_editor.insert(0,self.eachStudent[3])
                self.admin_professor_name_editor.insert(0,self.eachStudent[4])
                self.admin_grade_editor.insert(0,self.eachStudent[5])

            self.admin_editor_button=Button(self.admin_recordEditor,text="UPDATE RECORD",command=self.updateRecord)
            self.admin_editor_close_button = Button(self.admin_recordEditor, text="CANCEL",command=self.admin_recordEditor.destroy)
            self.admin_editor_button.grid(row=7,column=0,padx=20,pady=10,ipadx=20)
            self.admin_editor_close_button.grid(row=7,column=1,padx=20,pady=10,ipadx=30)
            self.admin_student_record.delete(0, END)
        else:
            print("Invalid Record ID")

    def updateRecord( self ):
        if int(self.admin_grade_editor.get()) >= 0 and int(self.admin_grade_editor.get()) <= 100:
            con_updateRecord = sqlite3.connect('SCHOOL_DATABASE.db')
            cursor_updateRecord = con_updateRecord.cursor()
            cursor_updateRecord.execute("""UPDATE STUDENT_RECORDS SET
                STUDENT_NUMBER = :stuid,
                STUDENT_NAME = :stuname,
                COURSE_NUMBER = :courseid,
                COURSE_NAME = :coursename,
                PROFESSOR_NAME = :prof,
                GRADE = :grade 
                WHERE oid = :oid""",
                      {
                          'stuid': self.admin_student_number_editor.get(),
                          'stuname': self.admin_student_name_editor.get(),
                          'courseid': self.admin_course_number_editor.get(),
                          'coursename': self.admin_course_name_editor.get(),
                          'prof': self.admin_professor_name_editor.get(),
                          'grade': self.admin_grade_editor.get(),
                          'oid': self.admin_student_record.get()
                      })
            self.admin_student_record.delete(0, END)
            con_updateRecord.commit()
            con_updateRecord.close()
            self.admin_recordEditor.destroy()
        else:
            tkinter.messagebox.showerror('Invalid','Invalid Grades')

    def deleteRecord( self ):
        if len(self.admin_student_record.get()) != 0:
            con_deleteRecord = sqlite3.connect('SCHOOL_DATABASE.db')
            cursor_deleteRecord = con_deleteRecord.cursor()
            cursor_deleteRecord.execute("DELETE from STUDENT_RECORDS WHERE oid = " + self.admin_student_record.get())
            self.admin_student_record.delete(0, END)
            con_deleteRecord.commit()
            con_deleteRecord.close()
        else:
            print("Invalid Record ID")

    def newLogin( self ):
        self.newLogin_window=Tk()
        self.newLogin_window.geometry('+400+200')
        self.newLogin_window.title("CREATE LOGIN CONSOLE")
        self.newLogin_window_Frame1 = Frame(self.newLogin_window)
        self.newLogin_window_Frame2 = Frame(self.newLogin_window)
        self.newLogin_window_Frame1.pack()
        self.newLogin_window_Frame2.pack()

        self.newLogin_label = Label(self.newLogin_window_Frame1, text="SIGN UP CONSOLE", font=("Times new Roman", 18))
        self.newLogin_userType = ''
        self.newLogin_type = IntVar()
        self.newLogin_type.set(1)
        self.newLogin_choice_admin = Radiobutton(self.newLogin_window_Frame1, text='Admin', variable=self.newLogin_type, value=1)
        self.newlogin_choice_prof = Radiobutton(self.newLogin_window_Frame1, text='Professor', variable=self.newLogin_type, value=2)
        self.newlogin_choice_student = Radiobutton(self.newLogin_window_Frame1, text='Student', variable=self.newLogin_type, value=3)

        self.newlogin_username_label = Label(self.newLogin_window_Frame2, text="USERNAME")
        self.newlogin_username = Entry(self.newLogin_window_Frame2, width=20)
        self.newlogin_password_label = Label(self.newLogin_window_Frame2, text="PASSWORD")
        self.newlogin_password = Entry(self.newLogin_window_Frame2, width=20, show="*")

        self.newlogin_login_button = Button(self.newLogin_window_Frame2, text="CREATE LOGIN", command=self.signUP)
        self.newlogin_signup_button = Button(self.newLogin_window_Frame2, text="CANCEL", command=self.newLogin_window.destroy)

        self.newLogin_label.grid(row=0, column=1, padx=20, pady=10)
        self.newLogin_choice_admin.grid(row=1, column=0)
        self.newlogin_choice_prof.grid(row=1, column=1)
        self.newlogin_choice_student.grid(row=1, column=2)
        self.newlogin_username_label.grid(row=2, column=0, padx=20, pady=10)
        self.newlogin_username.grid(row=2, column=1, padx=20, pady=10)
        self.newlogin_password_label.grid(row=3, column=0, padx=20)
        self.newlogin_password.grid(row=3, column=1, padx=20)
        self.newlogin_login_button.grid(row=4, column=0, padx=20, pady=20, ipadx=60)
        self.newlogin_signup_button.grid(row=4, column=1, padx=20, pady=20, ipadx=60)

    def signUP( self ):
        if self.newLogin_type.get()==1:
            self.master_userType='Admin'
        elif self.newLogin_type.get()==2:
            self.master_userType='Professor'
        elif self.newLogin_type.get()==3:
            self.master_userType='Student'

        connection_signupDB = sqlite3.connect('SCHOOL_DATABASE.db')
        # create cursor
        cursor_signupDB = connection_signupDB.cursor()

        if len(self.newlogin_username) == 0 or len(self.newlogin_password) == 0:
            tkinter.messagebox.showerror('ERROR', 'Empty Field NOT Allowed')
        else:
            try:
                cursor_signupDB.execute("INSERT INTO LOGIN_RECORDS VALUES (:LOGIN_TYPE,:USER_NAME,:USER_PASSWORD)",
                               {
                                   "LOGIN_TYPE": self.master_userType,
                                   "USER_NAME" : self.newlogin_username.get(),
                                   "USER_PASSWORD" : self.newlogin_password.get()
                               })
                tkinter.messagebox.showinfo('Successfull','Signup Successfull')
            except:
                tkinter.messagebox.showwarning('WARNING','User already exists')

        connection_signupDB.commit()
        connection_signupDB.close()
        self.newlogin_username.delete(0,END)
        self.newlogin_password.delete(0,END)


