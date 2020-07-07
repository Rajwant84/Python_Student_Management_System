from tkinter import *
import sqlite3
import tkinter.messagebox

class Professor:
    def __init__(self,prof_window):
        connection_newDB = sqlite3.connect('SCHOOL_DATABASE.db')
        # create cursor
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

        self.professor_window = prof_window
        self.professor_window.geometry("450x400+350+100")
        self.professor_window.title("PROFESSOR")

        self.professor_window_Frame1 = Frame(self.professor_window)
        self.professor_window_Frame2 = Frame(self.professor_window)
        self.professor_window_Frame1.pack()
        self.professor_window_Frame2.pack()
        self.Frame1_LabelHead = Label(self.professor_window_Frame1, text="PROFESSOR CONSOLE",font=("Times new Roman", 18))
        self.Frame1_LabelHead.pack()

        self.prof_student_number_label = Label(self.professor_window_Frame2, text="STUDENT NUMBER")
        self.prof_student_number = Entry(self.professor_window_Frame2, width=30)
        self.prof_student_name_label = Label(self.professor_window_Frame2, text="STUDENT NAME")
        self.prof_student_name = Entry(self.professor_window_Frame2, width=30)
        self.prof_course_number_label = Label(self.professor_window_Frame2, text="COURSE NUMBER")
        self.prof_course_number = Entry(self.professor_window_Frame2, width=30)
        self.prof_course_name_label = Label(self.professor_window_Frame2, text="COURSE NAME")
        self.prof_course_name = Entry(self.professor_window_Frame2, width=30)
        self.prof_professor_name_label = Label(self.professor_window_Frame2, text="PROFESSOR NAME")
        self.prof_professor_name = Entry(self.professor_window_Frame2, width=30)
        self.prof_grade_label = Label(self.professor_window_Frame2, text="GRADES")
        self.prof_grade = Entry(self.professor_window_Frame2, width=30)

        self.prof_insert_button = Button(self.professor_window_Frame2, text="ADD NEW RECORD", command=self.newRecord)
        self.prof_student_record_reset_button = Button(self.professor_window_Frame2, text="RESET",command=self.reset)
        self.prof_exit_button = Button(self.professor_window_Frame2, text="LOG OUT", command=self.professor_window.destroy)

        self.prof_student_number_label.grid(row=0, column=0)
        self.prof_student_number.grid(row=0, column=1, padx=20)
        self.prof_student_name_label.grid(row=1, column=0)
        self.prof_student_name.grid(row=1, column=1, padx=20)
        self.prof_course_number_label.grid(row=2, column=0)
        self.prof_course_number.grid(row=2, column=1, padx=20)
        self.prof_course_name_label.grid(row=3, column=0)
        self.prof_course_name.grid(row=3, column=1, padx=20)
        self.prof_professor_name_label.grid(row=4, column=0)
        self.prof_professor_name.grid(row=4, column=1, padx=20)
        self.prof_grade_label.grid(row=5, column=0)
        self.prof_grade.grid(row=5, column=1, padx=20)
        self.prof_insert_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)
        self.prof_student_record_reset_button.grid(row=10, column=0, columnspan=2, pady=10, ipadx=175)
        self.prof_exit_button.grid(row=12, column=0, columnspan=2, pady=10, ipadx=165)

    def newRecord( self ):
        if (len(self.prof_student_number.get()) != 0 or len(self.prof_student_name.get())) !=0 and len(self.prof_grade.get()) != 0:
            if int(self.prof_grade.get())>=0 and int(self.prof_grade.get()) <=100:
                #create Connection
                con_insert = sqlite3.connect('SCHOOL_DATABASE.db')
                cursor_insert = con_insert.cursor()
                cursor_insert.execute(
                    "INSERT INTO STUDENT_RECORDS VALUES (:stu_id, :stu_name, :course_id, :course_name, :prof_name, :grade)",
                    {
                        'stu_id': self.prof_student_number.get(),
                        'stu_name': self.prof_student_name.get(),
                        'course_id': self.prof_course_number.get(),
                        'course_name': self.prof_course_name.get(),
                        'prof_name': self.prof_professor_name.get(),
                        'grade': self.prof_grade.get()
                    })
                con_insert.commit()
                con_insert.close()

                self.prof_student_number.delete(0, END)
                self.prof_student_name.delete(0, END)
                self.prof_course_number.delete(0, END)
                self.prof_course_name.delete(0, END)
                self.prof_professor_name.delete(0, END)
                self.prof_grade.delete(0, END)
            else:
                print("Invalid Grades, OUT OF LIMIT")
        else:
            print("Empty fields not allowed")

    def reset( self ):
        self.prof_student_number.delete(0, END)
        self.prof_student_name.delete(0, END)
        self.prof_course_number.delete(0, END)
        self.prof_course_name.delete(0, END)
        self.prof_professor_name.delete(0, END)
        self.prof_grade.delete(0, END)
