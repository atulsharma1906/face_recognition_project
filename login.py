from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from main import Face_Recognition_System 
import tkinter as tk
import tkinter
from student import Student 
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance




def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        
        
        self.var_email=StringVar()
        self.var_pass=StringVar()
      
        #self.bg=ImageTk.PhotoImage(file=r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\bg.jpg")
       # lbl_bg=Label(self.root,image=self.bg)
       # lbl_bg.place(x=0,y=0,width=1535,height=710)
        
        img1=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\360_F_961274808_fX06eKzHJDCX9LO1Uew8YsL8Gk7RDZBu.jpg")    
        img1=img1.resize((1535,710),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1535,height=735)
        
        frame=Frame(self.root,bg="light grey")
        frame.place(x=200,y=160,width=340,height=450)
        
        img1=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\Screenshot 2024-12-22 180857.png")    
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=340,y=165,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black")
        get_str.place(x=120,y=100)
        
        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=65,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=65,y=220)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show='*')
        self.txtpass.place(x=35,y=250,width=270)
         #  icon image-------------
        img2=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\Screenshot 2024-12-22 180857.png")    
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg.place(x=238,y=313,width=25,height=25)
        
        img3=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\pass.png")    
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg.place(x=238,y=383,width=25,height=25)
          #login button 
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
         
         # register pass word 
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
         
         
         # forgot button 
        registerbtnbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        registerbtnbtn.place(x=15,y=370,width=160)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)    
        
    def login(self):
            if self.txtuser.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error", "All fields are required")
            elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
                messagebox.showinfo("Success", "Welcome")
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="atul123",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "SELECT * FROM register WHERE email=%s AND password=%s",
                        (self.txtuser.get(), self.txtpass.get())
                    )
                    row = my_cursor.fetchone()

                    if row is None:
                        messagebox.showerror("Error", "Invalid Username & Password")
                    else:
                        open_main = messagebox.askyesno("YesNo", "Access only admin")
                        if open_main:
                            self.new_window = Toplevel(self.root)
                            self.app = Face_Recognition_System(self.new_window)

                    conn.close()

                except Exception as e:
                    messagebox.showerror("Database Error", str(e))
                    
            #reset password
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
           messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", user="root",password="atul123", database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_securiy_Q.get(), self.txt_security.get(),)
            my_cursor.execute (qury, vlaue)
            row=my_cursor.fetchone()
            if row==None:
             messagebox.showerror("Error", "Plaese enter correct Answer",parent=self.root2)
            else:
             query=("update register set password=%s where email=%s")
             value=(self.txt_newpass.get(), self.txtuser.get())
             my_cursor.execute (query, value)
             
             conn.commit()
             conn.close()
             messagebox.showinfo("Info", "Your password has been reset,plaese login new password",parent=self.root2)
             self.root2.destroy()
                                 
                
            
     
    #-----------forgot password        
    def forgot_password_window(self):
        if self.txtuser.get()=="":
           messagebox.showerror("Error", "Plaese Wnter the Email address to reset password")
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.txtuser.get(),)
           my_cursor.execute(query, value)
           row=my_cursor.fetchone()
           #print(row ) 
           
           if row==None:
               messagebox.showerror("My Error","Please enter valid user name") 
           else:
               conn.close()
               self.root2=Toplevel()
               self.root2.title("Forgot Password")
               self.root2.geometry("340x450+610+170")
               l=Label(self.root2,text="Forgot",font=("times nre roman",20,"bold"),fg="red",bg="white")  
               l.place(x=0,y=10,relwidth=1)
               
              
                    
               security_Q=Label(self.root2, text="Select Security Quetions", font=("times new roman", 15, "bold"), bg="white", fg="black")
               security_Q.place(x=50,y=80)
                    
               self.combo_securiy_Q=ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
               self.combo_securiy_Q["values"]=("Select", "Your Birth Place",  "Your Pet Name")
               self.combo_securiy_Q.place(x=50,y=110, width=250)
               self.combo_securiy_Q.current(0)
                    
               security_A=Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
               security_A.place(x=50,y=150)
               self.txt_security=ttk.Entry(self.root2, font=("times new roman", 15,"bold"))
               self.txt_security.place(x=50,y=180,width=258)
               
               new_password=Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
               new_password.place(x=50,y=220)
               self.txt_newpass=ttk.Entry(self.root2, font=("times new roman", 15,"bold"))
               self.txt_newpass.place(x=50,y=250,width=258)
               
               btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15,"bold"),fg="white",bg="green")
               btn.place(x=100,y=290) 
               
class Register:
   def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        
        # vrables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        img1=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\flower.jpg")    
        img1=img1.resize((1535,710),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1535,height=735)
        
        #left img
        img2=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\reg.jpg")    
        img2=img2.resize((470,550),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbl_img=Label(self.root,image=self.photoimg2)
        lbl_img.place(x=50,y=100,width=470,height=550)
         ## frame 
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        #main Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame, text="REGISTER HERE", font =("times new roman", 25, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20,y=20)
        
        fname=Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50,y=100)
        
        frame_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        frame_entry.place(x=50,y=130, width=250)
        
        l_name=Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place (x = 370, y = 100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman",15))
        self.txt_lname.place( x = 370, y = 130,width=250)
     #--row2
        contact=Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place ( x = 50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place ( x = 50, y = 200, width=250)
        
        email=Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place ( x = 370, y = 200, width=250)
        
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        security_Q=Label(frame, text="Select Security Quetions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50,y=248)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"]=("Select", "Your Birth Place",  "Your Pet Name")
        self.combo_security_Q.place(x=50,y=280, width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370,y=240)
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.txt_security_A.place(x=370,y=270,width=258)
        
        pswd=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label (frame, text="Confirm Password",font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=378,y=318)
        
        self.txt_confirm_pswd=ttk.Entry (frame,textvariable=self.var_confpass, font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=348, width=250)
        
        self.var_check=IntVar()
        checkbtn=Checkbutton (frame,variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        img=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\unnamed.png")
        img=img.resize( (200,50), Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage, borderwidth=0,command=self.add_data, cursor="hand2",font=("times new roman", 15, "bold"))
        b1.place(x=10, y=420, width=200)
        
        img1=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\images.jpeg")
        img1=img1.resize( (200,50), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2",font=("times new roman", 15, "bold"))
        b1.place(x=330, y=420, width=200)
        
        #==============
   def add_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
              messagebox.showerror("Error", "All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get():
              messagebox.showerror("Error", "password & confirm password must be same")
            elif self.var_check.get()==0:
              messagebox.showerror("Error", "Plaese agree our terms ane condition")
            else:
             conn=mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
             my_cursor=conn.cursor()
             query=("select  * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query, value)
             row=my_cursor.fetchone()
             if row!=None:
              messagebox.showerror("Error", "User already exist, plaese try another email")
             else:
              my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)",(
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_securityQ.get(),
                                                                                     self.var_SecurityA.get(),
                                                                                     self.var_pass.get()
                                                                                    ))
             conn.commit()
             conn.close()
             messagebox.showinfo("Success", "Register Successfully")   
             
   def return_login(self):  
       self.root.destroy()  
             
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")




        img=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\image 2.png")    
        img=img.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        img1=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\face images.jpeg")    
        img1=img1.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

        img2=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\Facial Recognition Man Header.webp")    
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

        title_lbl=Label(bg_img,text="FACE   RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1535,height=45)
         
         #student button 
        img4=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\images.jpegstudents.jpeg")    
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=300,width=220,height=40)

        # detect face button 
        img5=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\face detection.jpeg")    
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=550,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=550,y=300,width=220,height=40)

     

       

         # train  face button 
        img8=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\train data.jpeg")    
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=580,width=220,height=40)

         # photos  face button 
        img9=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\photos.jpg")    
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=550,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=550,y=580,width=220,height=40)
        
        #attendence page 
        img10=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\0_Q2jXRZXXzEq2klcb.png")    
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.attendance_data)
        b1.place(x=900,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=300,width=220,height=40)

       

         # exit face button 
        img11=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\exit.png")    
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit,)
        b1.place(x=900,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=580,width=220,height=40)
        
    def open_img(self):
       os.startfile("data")
    #========function 
    
    def iExit(self):
      self.iExit=messagebox.askyesno("Face Recognition", "Are you sure exit this project", parent=self.root)
      if self.iExit >0:
          self.root.destroy()
      else:
         return

    def student_details(self):
     self.new_window=Toplevel(self.root)
     self.app=Student(self.new_window)
     
     
    def train_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Train(self.new_window)
    
     
    def face_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Face_Recognition(self.new_window)
     
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
                                    
                                                                                           
            





if __name__== "__main__":
    main()
   