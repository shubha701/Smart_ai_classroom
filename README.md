# 🎓 Smart AI Classroom Intelligence System

## 📌 Overview

Smart AI Classroom Intelligence System is an AI-powered classroom monitoring application that uses **YOLOv8 Object Detection** and **Streamlit** to automate classroom analysis. The system can detect students, chairs, desks, laptops, and other classroom objects in real-time from images, videos, and webcam feeds.

The project provides an interactive dashboard for classroom monitoring, object analytics, and attendance support, helping educational institutions improve classroom management and resource utilization.

---

## 🚀 Features

* ✅ Real-Time Object Detection using YOLOv8
* ✅ Classroom Monitoring and Analytics
* ✅ Student Detection
* ✅ Chair Detection
* ✅ Desk Detection
* ✅ Laptop Detection
* ✅ Image Upload Detection
* ✅ Video Upload Detection
* ✅ Webcam-Based Detection
* ✅ Interactive Dashboard
* ✅ Object Count Visualization
* ✅ Streamlit-Based User Interface
* ✅ Detection Statistics and Reports

---

## 🛠️ Technologies Used

### Programming Language

* Python

### AI / Machine Learning

* YOLOv8 (Ultralytics)

### Frontend

* Streamlit

### Libraries

* OpenCV
* Pandas
* NumPy
* Pillow (PIL)
* Plotly
* Collections

---

## 📂 Project Structure

```text
smart-ai-classroom/
│
├── app.py
├── yolov8n.pt
├── requirements.txt
├── assets/
│   ├── logo.png
│   └── banner.jpg
│
├── data/
│   └── attendance.csv
│
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/smart-ai-classroom.git
cd smart-ai-classroom
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Packages

```bash
pip install streamlit
pip install ultralytics
pip install opencv-python
pip install pandas
pip install pillow
pip install plotly
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🖼️ Detection Modules

### Dashboard

Displays:

* Model Information
* Classroom Analytics
* Detection Statistics
* System Status

### Image Detection

* Upload classroom images
* Detect students and classroom objects
* View object counts and analytics

### Video Detection

* Upload classroom videos
* Perform frame-by-frame object detection
* Display annotated results

### Live Camera Detection

* Capture classroom images
* Run real-time object detection
* Visualize detection results instantly

---

## 📊 Analytics

The system provides:

* Object Count Analysis
* Classroom Occupancy Monitoring
* Student Presence Statistics
* Detection Summary Reports
* Interactive Plotly Charts

---



## 👨‍💻 Author

**Shubha Prasad Sahoo**

AI & Data Science Enthusiast

---

## 📄 License

This project is intended for educational and academic purposes.
