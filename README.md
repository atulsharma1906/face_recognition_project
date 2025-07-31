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
│
├── attendance.py # Attendance marking module
├── data_set_generator.py # Capture face data
├── train.py # Train the LBPH face recognizer
├── face_recognition.py # Real-time face recognition & attendance
├── student.py # Add/edit student details
├── main.py # Main GUI application
├── python_connect_to_mysql.py # MySQL connectivity
├── images/ # GUI and icon assets
├── dataset/ # Captured face data
├── login.py/ # login
├── attendance/ # CSV files for attendance logs
└── README.md # Project overview and usage


---



