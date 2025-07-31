from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #============= variables==
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar() 
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()


        img=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\s3.jpeg")    
        img=img.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        img1=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\student 1.jpeg")    
        img1=img1.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

        img2=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\s2.webp")    
        img2=img2.resize((550,150),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=150)

        #bg image

        img3=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\133551190641011469.jpg")    
        img3=img3.resize((1535,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1535,height=710)

        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1535,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1505 ,height=575)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=555)

        img_left=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\s5.webp")    
        img_left=img_left.resize((750,100),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=120)

        #current course 

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information ",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=105,width=750,height=115)
         
         #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","MCA","B.TECH","BBA","B.PHARMA","MBA","M.TECH","Others")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1 ,padx=2,pady=10,sticky=W)

        #course 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","CSE","IT","Others")
        course_combo.current(0)
        course_combo.grid(row=0,column=3 ,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1 ,padx=2,pady=10,sticky=W)

        #semester 
    
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3 ,padx=2,pady=10,sticky=W)

        #current  student  

        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Student information ",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=230,width=750,height=300)

        #student id

        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name 

        studentName_label=Label(class_Student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # student section  

        studentSection_label=Label(class_Student_frame,text="Section :",font=("times new roman",12,"bold"),bg="white")
        studentSection_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #studentSection_entry=ttk.Entry(class_Student_frame,textvariable=self.var_sec,width=20,font=("times new roman",12,"bold"))
        #tudentSection_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
 
        secction_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_sec,font=("times new roman",12,"bold"),state="readonly",width=18)
        secction_combo["values"]=("A","B","C","D","E")
        secction_combo.current(0)
        secction_combo.grid(row=1,column=1 ,padx=10,pady=5,sticky=W)

        # roll no, 

        studentRollNO_label=Label(class_Student_frame,text="Roll NO. :",font=("times new roman",12,"bold"),bg="white")
        studentRollNO_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentRollNO_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        studentRollNO_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender 

        studentGender_label=Label(class_Student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        studentGender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #studentGender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #studentGender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1 ,padx=10,pady=5,sticky=W)

        # DOB

        DOB_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email

        Email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone number 

        phoneNumber_label=Label(class_Student_frame,text="Phone NO.:",font=("times new roman",12,"bold"),bg="white")
        phoneNumber_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneNumber_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phoneNumber_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # address 

        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # radio button
        self.var_radio1=StringVar() 
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

    
        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="NoPhoto Sample",value="No")
        radionbtn2.grid(row=6,column=1)

        #button frame 

        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=600,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=4)

        update_photo_btn=Button(btn_frame1,command=self.update_data,text="Update Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=4)

      








        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=710,height=555)

        img_right=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\s5.webp")    
        img_right=img_right.resize((750,100),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=750,height=120)

        # search system---------------

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System ",font=("times new roman",12,"bold"))
        search_frame.place(x=4,y=125,width=700,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_NO","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        ShowAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)

        #table frame----------

        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=5,y=210,width=695,height=300)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","sec","roll","gender","dob","email","phone no","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("roll",text="Roll NO.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no",text="Phone NO")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatuss")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width="100")
        self.student_table.column("year",width="100")
        self.student_table.column("sem",width="100")
        self.student_table.column("id",width="100")
        self.student_table.column("name",width="100")
        self.student_table.column("sec",width="100")
        self.student_table.column("roll",width="100")
        self.student_table.column("gender",width="100")
        self.student_table.column("dob",width="100")
        self.student_table.column("email",width="100")
        self.student_table.column("phone no",width="100")
        self.student_table.column("address",width="100")
        self.student_table.column("photo",width="150")
       


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

  #====== function declaration      
    def add_data(self):
          if self.var_dep.get()=="Select Department " or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
          else:
             try:
                conn=mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(), 
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_sec.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get()

                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success,Student details has been added Succefully",parent=self.root)
             except Exception as es:
                 messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

   #=============fetch data========

    def fetch_data(self):
     conn=mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
     my_cursor=conn.cursor()
     my_cursor.execute("select * from student")
     data=my_cursor.fetchall()

     if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
            self.student_table.insert("",END,values=i)
            conn.commit()
            # conn.close()

   #==========get cursor
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0]),
       self.var_course.set(data[1]),
       self.var_year.set(data[2]),
       self.var_semester.set(data[3]),
       self.var_std_id.set(data[4]),
       self.var_std_name.set(data[5]),
       self.var_sec.set(data[6]),
       self.var_roll.set(data[7]),
       self.var_gender.set(data[8]),
       self.var_dob.set(data[9]),
       self.var_email.set(data[10]),
       self.var_phone.set(data[11]),
       self.var_address.set(data[12]),
       self.var_radio1.set(data[13])

    # update ====
    def update_data(self):
        if self.var_dep.get()=="Select Department " or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
               Update=messagebox.askyesno("Update","DO you want to update this details ",parent=self.root)
               if Update>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
                my_cursor=conn.cursor() 
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Photo_Sample=%s where Std_id=%s",(
                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(), 
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                    self.var_sec.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                    ))
               else:
                  if not Update:
                     return
               messagebox.showinfo("Success","Student details successfully update complete",parent=self.root)  
               conn.commit()
               self.fetch_data()
               conn.close()
            except Exception as es:
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
  # delete function
    def delete_data(self):
       if self.var_std_id.get()=="":
          messagebox.showerror("Error","Student id must be required",parent=self.root)
       else:
          try:
              delete=messagebox.askyesno("Delete","DO you want to delete this student ",parent=self.root)
              if delete>0:
               conn=mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
               my_cursor=conn.cursor() 
               sql="delete from student where Std_id=%s"
               val=(self.var_std_id.get(),) 
               my_cursor.execute(sql,val)
              else:
               if not delete:
                 return
             
              conn.commit()
              self.fetch_data()
              conn.close()
          except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
   # reset =
    def reset_data(self):
       self.var_dep.set("Select Department"),
       self.var_course.set("Select Course"),
       self.var_year.set("Select year"),
       self.var_semester.set("Select Semester"),
       self.var_std_id.set(""),
       self.var_std_name.set(""),
       self.var_sec.set("Select Section"),
       self.var_roll.set(""),
       self.var_gender.set(""),
       self.var_dob.set(""),
       self.var_email.set(""),
       self.var_phone.set(""),
       self.var_address.set(""),
       self.var_radio1.set("")

  #=== generate data set or take photo sample
    def generate_dataset(self):  
      if not os.path.exists("data"):
       os.makedirs("data") 
      if self.var_dep.get()=="Select Department " or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
           try:
              
                conn=mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                #id=0
                #@for x in myresult:
                #   id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Photo_Sample=%s where Std_id=%s",(
                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(), 
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                    self.var_sec.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                #yeself.reset_data()
                conn.close() 

                #==========load predefined data on face  fontals from opencv
                face_classifier=cv2.CascadeClassifier("C:\\Users\\atuls\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml") 

                def face_cropped(img):
                  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
                  faces=face_classifier.detectMultiScale(gray,1.3,5)
                  #scalling factor=1.3
                  # minimum neighbor=5
                  
                  for(x,y,w,h) in faces:
                     face_cropped=img[y:y+h,x:x+w]
                     return face_cropped
                print("Student ID:", self.var_std_id.get())  
                cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id=0
                while True:
                  ret,my_frame=cap.read()
                  if face_cropped(my_frame) is not None:
                     img_id+=1
                     face=cv2.resize(face_cropped(my_frame),(450,450))
                     face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                     file_name_path="data/user"+str(self.var_std_id.get())+"."+str(img_id)+".jpg"
                     cv2.imwrite(file_name_path,face)
                     cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                     cv2.imshow("crooped Face",face)

                  if cv2.waitKey(1)==13 or img_id==100:
                     break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set compled !!!")
           except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)      
               

                                                                                                                                                               
                        
        
                 

              

        



                  
        
        


       


        





if __name__== "__main__":
   root=Tk()
   obj=Student(root)
   root.mainloop()

        



       