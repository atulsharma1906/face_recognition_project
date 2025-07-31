from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox  
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        #++++++++++variable 
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar() 
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

       
        
        # 2nd image
        
        img_bottom=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\4236e8efe43ae4a6c7f42c932aa3c01b.jpg")
        
        img_bottom=img_bottom.resize((1530,200), Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk. PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0, y = 0, width=1530, height=200)
        
        img3 = Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\133551190641011469.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman", 35, "bold"),fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)
        
        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=500)

        img_left=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\s5.webp")    
        img_left=img_left.resize((750,100),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=120)
        
        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=300)
         
        attendenceId_label=Label(left_inside_frame,text="Attendence_ID:",font=("times new roman",12,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        Name_label=Label(left_inside_frame,text="Name :",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0)

        atten=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten.grid(row=1,column=1,pady=8)
        
        roll_label=Label(left_inside_frame,text="Roll No. :",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)
        
        dep_label=Label(left_inside_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        time_label=Label(left_inside_frame,text="Time :",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)
        
        date_label=Label(left_inside_frame,text="Date :",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,pady=8)
        
        attendence_label=Label(left_inside_frame,text="Attendence Status :",font=("times new roman",12,"bold"),bg="white")
        attendence_label.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["value"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #button frame 

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=265,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

       # delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        #delete_btn.grid(row=0,column=2)

        #Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
       # Reset_btn.grid(row=0,column=3)
        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=680,height=500)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=665,height=450)
        
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,show="headings")
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        
        
        self.AttendenceReportTable.heading("id",text="Attendance ID")
        self.AttendenceReportTable.heading("roll", text="Roll No.")
        self.AttendenceReportTable.heading("name", text="Name")
        self.AttendenceReportTable.heading("department", text="Department")
        self.AttendenceReportTable.heading("time", text="Time")
        self.AttendenceReportTable.heading("date", text="Date")
        self.AttendenceReportTable.heading("attendence", text="Attendance")
        
        self.AttendenceReportTable.column("id", width=100)
        self.AttendenceReportTable.column("roll", width=100)
        self.AttendenceReportTable.column("name", width=150)
        self.AttendenceReportTable.column("department", width=150)
        self.AttendenceReportTable.column("time", width=100)
        self.AttendenceReportTable.column("date", width=100)
        self.AttendenceReportTable.column("attendence", width=100)
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
    def fetchData(self,rows):
       self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
       for i in rows:
           self.AttendenceReportTable.insert("",END,value=i)
                
    def importcsv(self):
            global mydata
            mydata.clear()
            fln = filedialog.askopenfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
            if fln == "":  # User cancelled the dialog
                return

            try:
                with open(fln) as myfile:
                    csvread = csv.reader(myfile)
                    for row in csvread:
                        mydata.append(row)
                    self.fetchData(mydata)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file\n{str(e)}", parent=self.root)
    
   ### export csV 
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False

        # Get file location from save dialog
            fln = filedialog.asksaveasfilename(
             initialdir=os.getcwd(),
             title="Save CSV",
             defaultextension=".csv",
             filetypes=(("CSV File", "*.csv"),),
             parent=self.root
            )

            if fln:  # If user did not cancel the dialog
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for row in mydata:
                      exp_write.writerow(row)

                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
          messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_focus=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_focus)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
   # def reset_data(self):
       ### self.var_atten_roll.set(" ")
       # self.var_atten_name.set(" ")
       # self.var_atten_dep.set(" ")
       # self.var_atten_time.set(" ")
       # self.var_atten_date.set(" ")
       # self.var_atten_attendance.set(" ")
            
if __name__== "__main__":
           root=Tk()
           obj=Attendance(root)
           root.mainloop()        