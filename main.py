from tkinter import*
from tkinter import ttk
import tkinter as tk
import os
import tkinter
from student import Student 
from PIL import Image,ImageTk
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import messagebox



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

        img3=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\backgroung.jpg")    
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

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
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
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

