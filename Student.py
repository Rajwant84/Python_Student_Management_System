from tkinter import *
import sqlite3

class Student:
    def __init__(self,stu_window):
        self.stu_window=stu_window
        self.stu_window.geometry("400x500+350+100")
        self.stu_window.title("STUDENT")
        self.stu_head_label=Label(self.stu_window,text="STUDENT CONSOLE",font=("Times new Roman", 18))
        self.stu_student_number_label=Label(self.stu_window,text="STUDENT NUMBER")
        self.stu_student_number=Entry(self.stu_window,width=30)
        self.stu_showgrades_button=Button(self.stu_window,text="STUDENT DATA",command=self.stuQuery)
        self.stu_exit_button=Button(self.stu_window,text="SIGN OUT",command=self.stu_window.destroy)

        self.stu_head_label.grid(row=0,column=0,padx=20,pady=20,columnspan=3)
        self.stu_student_number_label.grid(row=1,column=0,padx=20)
        self.stu_student_number.grid(row=1,column=1,padx=20)
        self.stu_showgrades_button.grid(row=2,column=0,padx=20,pady=20,columnspan=3)
        self.stu_exit_button.grid(row=3,column=0,padx=20,columnspan=3)

    def stuQuery( self ):
        conn_showRecord = sqlite3.connect('SCHOOL_DATABASE.db')

        cursor_showRecord = conn_showRecord.cursor()

        cursor_showRecord.execute("SELECT *, oid FROM STUDENT_RECORDS")
        records = cursor_showRecord.fetchall()

        print_records = ''
        headingLabel = "Student ID"+ "\t" + "Stu Name"+ "\t" + "Course Name"+ "\t" + "Grades"
        for record in records:
            if str(record[0]) == self.stu_student_number.get():
                print_records = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[3]) + "\t\t" + str(record[5]) + "\n"

        heading_label = Label(self.stu_window, text=headingLabel)
        heading_label.grid(row=4, column=0, columnspan=3)

        query_label = Label(self.stu_window, text=print_records)
        query_label.grid(row=5, column=0, columnspan=3)

        # Commit Changes
        conn_showRecord.commit()

        # Close Connection
        conn_showRecord.close()