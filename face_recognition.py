from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox  
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from mysql.connector import Error



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        
        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"),bg="white",fg="blue")
        title_lbl.place( x = 0 ,y=0,width=1530,height=45)
        
        #    first image
        img_top=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\images (1).jpeg")
        img_top=img_top.resize((650,700), Image.Resampling.LANCZOS)
        
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y = 55, width=655, height=700)
        
        # 2nd image
        
        img_bottom=Image.open(r"C:\Users\atuls\OneDrive\Desktop\face recognition system\college_images\0f5b34d0267977235d8f3d0d943de459.jpg")
        
        img_bottom=img_bottom.resize((950,700), Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk. PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650, y = 55, width=950, height=700)
        #button
        b1_1=Button(self.root,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="green",fg="white")
        b1_1.place(x=700,y=620,width=200,height=40)
    #=====attendence

    def mark_attendence(self, std_id, roll, name, dep):
         
        
         filename = "Atul.csv"
         entry_found = False
         today = datetime.now().strftime("%d/%m/%Y")

         try:
            
             with open(filename, "r+", newline='') as f:
                 lines = f.readlines()
                 for line in lines:
                     parts = line.strip().split(",")
                     if len(parts) >= 6:
                         if parts[0] == std_id and parts[1] == roll and parts[2] == name and parts[3] == dep and parts[5] == today:
                             entry_found = True
                             break

                 if not entry_found:
                     now = datetime.now()
                     time_str = now.strftime("%H:%M:%S")
                     f.write(f"\n{std_id},{roll},{name},{dep},{time_str},{today},Present")

         except FileNotFoundError:
            # File doesn't exist yet, create it and write header + first row
              with open(filename, "w", newline='') as f:
                 f.write("Std_ID,Roll,Name,Department,Time,Date,Status\n")
                 now = datetime.now()
                 time_str = now.strftime("%H:%M:%S")
                 f.write(f"{std_id},{roll},{name},{dep},{time_str},{today},Present")
                    
                
    #==========face recognition 
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
          gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
          coord=[]
         
          for (x,y,w,h) in features:
              cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
              id,predict=clf.predict(gray_image[y:y+h,x:x+w])
              confidence=int((100*(1 - predict / 300)))
              print(f"[DEBUG] ID: {id}, Confidence: {confidence}")
              try:
                 
             # n, r, d = "Name", "Roll", "Dep"
                 conn =mysql.connector.connect(host="localhost",user="root",password="atul123",database="face_recognizer")
                 my_cursor=conn.cursor()
                    
                 my_cursor.execute("SELECT Name, Roll, Dep, Std_id FROM student WHERE Std_id = %s", (str(id),))
                 result = my_cursor.fetchone()

                 if result:
                     name, roll, dep, std_id = result
                     print(f"[DEBUG] Match Found - ID: {std_id}, Name: {name}")
                 else:
                    print("No record found for the given Std_id.")
                    name = roll = dep = std_id = "Not Found"
                    
                 conn.close()
              except mysql.connector.Error as err:
                 
                 print(f"Error: {err}")
                 continue  # Skip to the next face if there's an error
            
             
             
              if confidence > 75:
                 cv2.putText(img,f"Std_id:{std_id}",(x,y-77 ),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f"Name:{name}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f"Roll:{roll}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f"Dep:{dep}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 self.mark_attendence(std_id,roll,name,dep)
              else:
                 cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255),2)
                 cv2.putText(img,"Unknown Face",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2) 
                 
              coord=[x,y,w,h]
             
          return coord
     
        def recognize(img,clf, faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255, 25,255), "Face", clf)
            return img
        
        
        faceCascade = cv2.CascadeClassifier("C:\\Users\\atuls\\OneDrive\\Desktop\\face recognition system\\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()  
                        
        
if __name__== "__main__":
   root=Tk()
   obj=Face_Recognition(root)
   root.mainloop()       