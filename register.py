from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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
        b1=Button(frame,image=self.photoimage1, borderwidth=0, cursor="hand2",font=("times new roman", 15, "bold"))
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


        
           
             
            
        
    
        
        
if __name__== "__main__":
   root=Tk()
   app=Register(root)
   root.mainloop()        
        
        