import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import tempfile
import pandas as pd
import plotly.express as px
from collections import Counter

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Smart AI Classroom",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

.block-container {
    padding-top: 1rem;
}

.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    text-align:center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

.big-font {
    font-size:40px;
    font-weight:bold;
    color:#2563EB;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <h1 style='text-align:center;color:#2563EB'>
    🎓 Smart AI Classroom Intelligence System
    </h1>

    <h4 style='text-align:center'>
    Real-Time Classroom Monitoring Using YOLOv8
    </h4>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=120
)

st.sidebar.title("Smart AI Classroom")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Image Detection",
        "Video Detection",
        "Live Camera"
    ]
)

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if page == "Dashboard":

    st.markdown("## 📊 System Dashboard")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
        <h2>🎯 YOLOv8</h2>
        <p>Detection Engine</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h2>👨‍🎓 Students</h2>
        <p>Attendance Tracking</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h2>💺 Furniture</h2>
        <p>Chair & Desk Detection</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
        <h2>📈 Analytics</h2>
        <p>Live Insights</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Project Features")

    st.success("✅ Student Detection")
    st.success("✅ Chair Detection")
    st.success("✅ Desk Detection")
    st.success("✅ Laptop Detection")
    st.success("✅ Attendance Dashboard")
    st.success("✅ Real-Time Monitoring")

# --------------------------------------------------
# IMAGE DETECTION
# --------------------------------------------------

elif page == "Image Detection":

    st.title("🖼 Image Detection")

    image_file = st.file_uploader(
        "Upload Classroom Image",
        type=["jpg","jpeg","png"]
    )

    if image_file:

        image = Image.open(image_file)

        model = load_model()

        with st.spinner("Detecting Objects..."):
            results = model(image)

        annotated = results[0].plot()

        col1,col2 = st.columns(2)

        with col1:
            st.image(
                image,
                caption="Original Image",
                use_container_width=True
            )

        with col2:
            st.image(
                annotated,
                caption="Detection Result",
                use_container_width=True
            )

        names = model.names

        detected = []

        for box in results[0].boxes:
            cls = int(box.cls[0])
            detected.append(names[cls])

        counter = Counter(detected)

        if len(counter) > 0:

            st.subheader("Detected Objects")

            df = pd.DataFrame(
                counter.items(),
                columns=["Object","Count"]
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            fig = px.pie(
                df,
                values="Count",
                names="Object",
                title="Object Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# --------------------------------------------------
# VIDEO DETECTION
# --------------------------------------------------

elif page == "Video Detection":

    st.title("🎥 Video Detection")

    video = st.file_uploader(
        "Upload Video",
        type=["mp4","avi","mov"]
    )

    if video:

        st.video(video)

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )

        temp_file.write(video.read())

        video_path = temp_file.name

        if st.button("Start Detection"):

            model = load_model()

            cap = cv2.VideoCapture(video_path)

            frame_placeholder = st.empty()

            while cap.isOpened():

                ret, frame = cap.read()

                if not ret:
                    break

                results = model(frame)

                frame = results[0].plot()

                frame_placeholder.image(
                    frame,
                    channels="BGR",
                    use_container_width=True
                )

            cap.release()

            st.success("Video Processing Completed")

# --------------------------------------------------
# LIVE CAMERA
# --------------------------------------------------

elif page == "Live Camera":

    st.title("📷 Live Camera Detection")

    camera = st.camera_input(
        "Capture Classroom Image"
    )

    if camera:

        image = Image.open(camera)

        model = load_model()

        results = model(image)

        annotated = results[0].plot()

        col1,col2 = st.columns(2)

        with col1:
            st.image(
                image,
                use_container_width=True
            )

        with col2:
            st.image(
                annotated,
                use_container_width=True
            )

        names = model.names

        detected = []

        for box in results[0].boxes:
            cls = int(box.cls[0])
            detected.append(names[cls])

        counter = Counter(detected)

        if detected:

            df = pd.DataFrame(
                counter.items(),
                columns=["Object","Count"]
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            fig = px.bar(
                df,
                x="Object",
                y="Count",
                title="Detected Objects"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )