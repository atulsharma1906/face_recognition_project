import tkinnter 
from tkinter import*
from tkinter import ttk
import numpy as np
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
from PIL import Image,ImageTk

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
        b1_1.place(x=880,y=620,width=200,height=40)

# Load classifier
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier1.xml")  # Ensure this file exists

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="atul123",
    database="face_recognizer"
)
cursor = conn.cursor()

# Load face cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initialize webcam
video = cv2.VideoCapture(0)

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, recognizer):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)

    for (x, y, w, h) in features:
        id_, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if confidence < 70:
            # Fetch student info from DB
            cursor.execute("SELECT Name, Dep  FROM student WHERE Std_id = %s", (id_,))
            result = cursor.fetchone()

            if result:
                name, department = result
                cv2.putText(img, f"Name: {name}", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                cv2.putText(img, f"Dept: {department}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            else:
                cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        else:
            cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    return img

while True:
    ret, frame = video.read()
    frame = draw_boundary(frame, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 13:  # Press Enter to exit
        break

video.release()
cv2.destroyAllWindows()
cursor.close()
conn.close()


if __name__== "__main__":
   root=Tk()
   obj=Face_Recognition(root)
   root.mainloop()