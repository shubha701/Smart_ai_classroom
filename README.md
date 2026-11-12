# 🎓 Smart AI Classroom – AI-Powered Classroom Monitoring System

An intelligent classroom monitoring and management system built using **Python, YOLOv8, Computer Vision, and Streamlit**. The application uses real-time object detection to monitor classroom environments, identify students and classroom objects, and provide an interactive dashboard for classroom insights.

## 🚀 Project Overview

Smart AI Classroom is an AI-powered application designed to make classroom monitoring smarter, faster, and more efficient.

Using the YOLOv8 object detection model, the system detects classroom-related objects from uploaded images, videos, and live webcam streams. It provides an interactive Streamlit interface with a dashboard for monitoring and visualizing classroom activity.

The project aims to demonstrate how Artificial Intelligence and Computer Vision can be applied to modern educational environments.

## ✨ Key Features

- **AI-Based Object Detection:** Detects classroom objects using the YOLOv8 model.
- **Image Detection:** Upload images and identify classroom objects.
- **Video Detection:** Analyze uploaded classroom videos.
- **Live Webcam Detection:** Perform real-time object detection through a webcam.
- **Interactive Dashboard:** Display classroom monitoring insights.
- **Student Monitoring:** Identify students detected in the classroom.
- **Classroom Object Recognition:** Detect objects such as chairs, desks, and laptops.
- **User Authentication:** Login and signup functionality.
- **Streamlit Interface:** Simple and interactive web-based user interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLOv8 | Object detection model |
| Ultralytics | YOLOv8 implementation |
| Streamlit | Web application framework |
| OpenCV | Image and video processing |
| NumPy | Numerical operations |
| Computer Vision | Visual object recognition |

## 🏗️ System Architecture


              SMART AI CLASSROOM
                      |
                      v
              Streamlit Interface
                      |
             User Authentication
                      |
                      v
               Input Selection
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Image        Video       Webcam
          |           |           |
          +-----------+-----------+
                      |
                      v
              OpenCV Processing
                      |
                      v
                YOLOv8 Model
                      |
                      v
              Object Detection
                      |
                      v
             Detection Results
                      |
                      v
             Interactive Dashboard



## 🧠 Model Information

This project uses **YOLOv8 (You Only Look Once)**, an advanced real-time object detection model developed by Ultralytics.

The model processes visual input and identifies objects by generating bounding boxes and class labels.

**Detection capabilities include:**
- Students
- Chairs
- Desks
- Laptops

The trained model weights are stored in the `models/` directory.

## 📸 Application Modules

The application consists of the following modules:

1. **Dashboard:** Displays classroom monitoring information and detection statistics.
2. **Upload Image:** Detects classroom objects from uploaded images.
3. **Upload Video:** Processes videos and displays object detection results.
4. **Live Webcam:** Performs real-time object detection using a webcam.

## 🎯 Objectives

- Automate classroom object detection using Artificial Intelligence.
- Explore real-time computer vision applications.
- Build an interactive classroom monitoring platform.
- Demonstrate the practical implementation of YOLOv8.
- Develop a foundation for intelligent classroom management systems.

## 🔮 Future Enhancements

- Automated attendance management.
- Student counting and tracking.
- Classroom activity analytics.
- Real-time notifications and alerts.
- Database integration for attendance records.
- Cloud-based deployment.
- Advanced classroom analytics and reporting.

## 👨‍💻 Developer

**Shubha Prasad Sahoo**

B.Tech – Data Science

Interested in Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision.

## ⭐ Support

If you find this project interesting or useful, consider giving this repository a ⭐ on GitHub.

---

**Built with ❤️ using Python, YOLOv8, Computer Vision, and Streamlit.**
