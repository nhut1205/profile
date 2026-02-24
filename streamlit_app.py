import streamlit as st
import cv2
import numpy as np
import joblib

# ======================
# 1. Page Configuration
# ======================
st.set_page_config(
    page_title="Nhut Pham | Engineering Portfolio", 
    page_icon="👨‍💻", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# 2. CryBean Helper Functions
# ======================
@st.cache_resource
def load_crybean_models():
    """Load model và label encoder (Dùng cache để tối ưu hiệu năng)"""
    try:
        rf_model = joblib.load("RandomForest_best_model.pkl")
        label_encoder = joblib.load("label_encoder.pkl")
        return rf_model, label_encoder
    except Exception as e:
        return None, None

def extract_full_features_from_image(image):
    """Trích xuất 16 đặc trưng hình học từ ảnh hạt đậu bằng OpenCV"""
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None

    largest_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest_contour)
    
    if area < 500:
        return None

    perimeter = cv2.arcLength(largest_contour, True)
    ellipse = cv2.fitEllipse(largest_contour)
    major_axis_length = max(ellipse[1])
    minor_axis_length = min(ellipse[1])

    aspect_ratio = major_axis_length / minor_axis_length
    compactness = area / (perimeter ** 2)
    circularity = (4 * np.pi * area) / (perimeter ** 2)
    eccentricity = np.sqrt(1 - (minor_axis_length / major_axis_length) ** 2)

    convex_hull = cv2.convexHull(largest_contour)
    convex_area = cv2.contourArea(convex_hull)
    equivalent_diameter = np.sqrt(4 * area / np.pi)

    bounding_rect = cv2.boundingRect(largest_contour)
    rect_area = bounding_rect[2] * bounding_rect[3]
    extent = area / rect_area 
    solidity = area / convex_area 
    roundness = (4 * area) / (np.pi * (major_axis_length ** 2)) 
    moments = cv2.moments(largest_contour)
    hu_moments = cv2.HuMoments(moments).flatten()

    features = np.array([area, perimeter, major_axis_length, minor_axis_length, 
                         aspect_ratio, compactness, circularity, eccentricity, 
                         convex_area, equivalent_diameter, rect_area, extent,
                         solidity, roundness, hu_moments[0], hu_moments[1]])
    return features

# Từ điển mô tả các loại đậu
bean_descriptions = {
    'DERMASON': "DERMASON là loại đậu có kích thước nhỏ, thường được sử dụng trong các món salad và súp.",
    'SEKECI': "Đậu SEKECI có kích thước trung bình, hình bầu dục và thường có màu nâu đậm.",
    'SORA': "Đậu SORA là loại đậu nhỏ, màu đen sẫm với bề mặt bóng loáng.",
    'BENGAL': "Đậu BENGAL có kích thước trung bình, với màu nâu nhạt.",
    'HOROZ' : "Đậu HOROZ có đặc điểm là hạt to, hình bầu dục và có thể có màu nâu hoặc nâu nhạt.",
    'SEKER' : "Đậu SEKER có kích thước nhỏ, bề mặt bóng loáng và có màu đen.",
    'PINK': "Đậu PINK nhỏ, tròn và có màu hồng nhạt. Thường dùng trong các món hầm.",
    'CANNELLINI': "Đậu CANNELLINI là loại đậu trắng lớn, kết cấu dạng kem, phổ biến trong ẩm thực Ý."
}   

# ======================
# 3. Page Rendering Functions
# ======================

def render_about():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 👋 Hello, I'm Pham Minh Nhut")
        st.markdown("""
        **Data Analyst | Tech Enthusiast**
        
        I am an IT Engineer with a deep passion for data and technology. 
        I focus on transforming raw data into actionable insights and building 
        efficient data workflows to solve real business problems.
        
        **Core Values:**
        * 📊 **Insight:** Meaningful business value over raw numbers
        * 🛠️ **Accuracy:** Data integrity and structured analysis over assumptions
        * ⚡ **Efficiency:** Automated and optimized data processes
        
        *Currently exploring advanced data analytics, predictive modeling, and data storytelling.*
        """)
    with col2:
        st.image("avatar.jpg.png", caption="Software Engineer")

def render_philosophy():
    st.markdown("### 🧠 Engineering Philosophy")
    st.info("**\"Solving real business problems rather than chasing trends.\"**", icon="💡")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("#### 📖 Readable\nCode is read much more often than it is written.")
    with col2:
        st.warning("#### 📈 Scalable\nBuilt to handle tomorrow's traffic, today.")
    with col3:
        st.error("#### 🧪 Testable\nConfidence through automated verification.")
    st.markdown("---")
    st.markdown("I heavily lean towards **Clean Architecture** mindsets. Separating the domain logic from the infrastructure ensures that the systems I build remain adaptable and testable regardless of changing external technologies.")

def render_projects():
    st.markdown("### 🚀 Selected Projects")
    
    # Project 1: Shifting focus from Web App to Database & API
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🎬 Movie Database & Data API")
            st.markdown("""
            Designed a relational database architecture and built API pipelines to manage and retrieve large-scale movie data.
            - **Data Modeling:** Designed and normalized database structures (Relational SQL) for complex, real-world datasets.
            - **Data Integration & API:** Built a RESTful API (ASP.NET) with optimized queries for high-speed data delivery to clients.
            - **Data Security:** Implemented JWT Authentication and Role-Based Access Control (RBAC) to secure data sources.
            """)
        with col2:
            st.link_button("View on GitHub", "https://github.com/yourlink")
            
    st.divider()
    
    # Project 2: CryBean - Emphasizing Data Extraction & Analytics
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🌱 CryBean: Quality Analytics & Predictive Modeling")
            st.markdown("""
            A geometric data analysis and Machine Learning system to automate the quality assessment process of agricultural products.
            - **Data Extraction:** Applied Computer Vision (OpenCV) to automatically extract and quantify 16 variables (features) from raw images.
            - **Predictive Analysis:** Trained, evaluated, and fine-tuned classification models (Random Forest, SVM, Neural Network) to identify the most optimal algorithm.
            - **Tech Stack:** Python, Pandas, Scikit-learn, OpenCV, Streamlit.
            """)
        with col2:
            st.link_button("View on GitHub", "https://github.com/nhut1205/CryBean.git")
    
    st.divider()
    
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🌱 CryBean: Bean Quality Assessment (Computer Vision)")
            st.markdown("""
            Hệ thống nhận diện và phân loại hạt đậu tự động sử dụng Machine Learning và Computer Vision.
            - **Feature Extraction:** Ứng dụng OpenCV để tự động trích xuất 16 thông số hình học từ ảnh.
            - **Machine Learning:** Huấn luyện và so sánh Random Forest, SVM, Neural Network để chọn ra mô hình tối ưu nhất.
            - **Tech Stack:** Python, OpenCV, Scikit-learn, Streamlit.
            """)
        with col2:
            st.link_button("View on GitHub", "https://github.com/nhut1205/CryBean.git")

def render_crybean_demo():
    st.markdown("### 🌱 Live Demo: CryBean Vision")
    st.markdown("Tải lên một bức ảnh hạt đậu khô (trên nền sáng/tương phản) để AI tự động trích xuất đặc trưng hình học và phân loại.")
    
    rf_model, label_encoder = load_crybean_models()
    
    if rf_model is None or label_encoder is None:
        st.error("⚠️ Không tìm thấy file `RandomForest_best_model.pkl` hoặc `label_encoder.pkl`. Vui lòng đặt chúng cùng thư mục với app.")
        return

    uploaded_file = st.file_uploader("Chọn ảnh hạt đậu...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Đọc và decode ảnh
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image_rgb, caption='Ảnh đã tải lên', use_container_width=True)
            
        with col2:
            with st.spinner('Đang dùng OpenCV trích xuất đặc trưng & phân tích...'):
                features = extract_full_features_from_image(image)
                
                if features is None:
                    st.error("❌ Không nhận diện được hạt đậu nào trong ảnh. Vui lòng thử ảnh khác có độ tương phản tốt hơn (hạt đậu trên nền trắng/sáng).")
                else:
                    features_reshaped = features.reshape(1, -1)
                    predicted_class = rf_model.predict(features_reshaped)
                    predicted_label = label_encoder.inverse_transform(predicted_class)[0]
                    description = bean_descriptions.get(predicted_label, "Không có mô tả cho loại đậu này.")
                    
                    st.success(f"🎉 **Dự đoán:** Đậu **{predicted_label.upper()}**")
                    st.info(f"**Mô tả:** {description}")
                    
                    with st.expander("🔍 Xem chi tiết các đặc trưng đã trích xuất (OpenCV)"):
                        st.json({
                            "Area": round(features[0], 2),
                            "Perimeter": round(features[1], 2),
                            "Major Axis Length": round(features[2], 2),
                            "Minor Axis Length": round(features[3], 2),
                            "Aspect Ratio": round(features[4], 4),
                            "Compactness": round(features[5], 4),
                            "Circularity": round(features[6], 4),
                            "Eccentricity": round(features[7], 4)
                        })

def render_tech_stack():
    st.markdown("### ⚙️ Technical Stack")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🧱 Backend")
        st.code("ASP.NET Web API\nC#\nSQL Server\nRESTful Design", language="text")
    with col2:
        st.markdown("#### 🤖 Data & AI")
        st.code("Python\nOpenCV\nScikit-learn\nPandas / Numpy", language="text")
    with col3:
        st.markdown("#### 🚀 Tools & UI")
        st.code("Streamlit\nDocker\nGit & GitHub", language="text")

def render_interests():
    st.markdown("### 📚 Beyond Coding")
    st.markdown("- System Design\n- Automation & Computer Vision\n- Backend Optimization\n- Thoughtful UI Design (8-bit / Chill vibes)")

# ======================
# 4. Sidebar Navigation & Contact
# ======================
with st.sidebar:
    st.title("Navigation")
    
    pages = {
        "👤 About": render_about,
        "🧠 Philosophy": render_philosophy,
        "🚀 Projects": render_projects,
        "🌱 Live Demo: CryBean": render_crybean_demo,
        "⚙️ Tech Stack": render_tech_stack,
        "📚 Interests": render_interests
    }
    
    selection = st.radio("Go to", list(pages.keys()), label_visibility="collapsed")
    
    st.divider()
    
    st.markdown("### 📬 Contact")
    st.markdown("📧 [nhuta4@gmail.com](mailto:nhuta4@gmail.com)")
    st.markdown("🔗 [LinkedIn Profile](#)")
    st.markdown("💻 [GitHub Profile](#)")
    
    st.caption("© 2026 Pham Minh Nhut")

# ======================
# 5. Main App Execution
# ======================
pages[selection]()