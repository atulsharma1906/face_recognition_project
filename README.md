# face_recognition_project


A Python-based Face Recognition Attendance System using OpenCV, MySQL, and Tkinter. This project captures real-time face data, stores student details, marks attendance using face recognition, and maintains attendance logs in a database.

## 📌 Features

- 👤 **Student Registration**: Add and update student details.
- 📸 **Face Dataset Generator**: Capture face images using a webcam.
- 🤖 **Face Training**: Train the recognition model with collected face data.
- 🧠 **Face Recognition**: Real-time recognition and automatic attendance marking.
- 🗓️ **Attendance Log**: Save and view attendance records.
- 💻 **User Interface**: GUI built with Tkinter.
- 🛢️ **Database Integration**: Uses MySQL for storing student info and attendance records.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV**
- **Tkinter**
- **MySQL** (with `mysql-connector-python`)
- **NumPy**
- **PIL (Pillow)**

---

## 📁 Project Structure
face_recognition_attendance/
├── README.md # Project documentation
├── attendance.py # Module for marking attendance
├── attendence sheet.csv # CSV file for logged attendance records
├── face_recognition.py # Face recognition functionality
├── haarcascade_frontalface_default.xml # Haar cascade classifier for face detection
├── login.py # Login system module
├── main.py # Main GUI launcher
├── python_connect_to_mysql.py # MySQL database connection handler
├── reconition.py # Alternate recognition logic (possibly outdated)
├── register.py # Register new users/faces
├── student.py # Manage student details
├── train.py # Train face recognition model





