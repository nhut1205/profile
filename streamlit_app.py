import streamlit as st

st.set_page_config(
    page_title="My Profile",
    page_icon="🚀",
    layout="wide"
)

# ===== Custom CSS =====
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
.big-title {
    font-size: 50px;
    font-weight: 700;
    background: -webkit-linear-gradient(#38bdf8, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# ===== Header =====
st.markdown('<div class="big-title">🚀 Pham Minh Nhut</div>', unsafe_allow_html=True)
st.subheader("💻 IT Engineer | Web API | SQL | Streamlit")

st.write("🔥 Đam mê xây dựng web app, tối ưu database và sáng tạo UI độc đáo.")

st.divider()

# ===== Layout 2 cột =====
col1, col2 = st.columns([1,2])

with col1:
    st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=180)
    st.markdown("### 🌐 Connect with me")
    st.markdown("""
    - 📧 nhuta4@gmail.com
    - 💼 LinkedIn
    - 🐙 GitHub
    """)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🛠 Skills")

    st.progress(90)
    st.write("C# / .NET")

    st.progress(85)
    st.write("SQL Server")

    st.progress(80)
    st.write("JavaScript")

    st.progress(75)
    st.write("Python")

    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ===== Project Section =====
st.markdown("## 🚀 Featured Projects")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    ### 🎬 Movie Web App
    - ASP.NET Web API
    - JWT Authentication
    - SQL Server
    """)

with col4:
    st.markdown("""
    ### 📊 Data Dashboard
    - Streamlit
    - Interactive Chart
    - Real-time data
    """)

st.divider()

st.caption("© 2026 Pham Minh Nhut | Built with ❤️ using Streamlit")