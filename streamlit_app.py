import streamlit as st

st.set_page_config(page_title="Engineering Portfolio", layout="wide")

# ======================
# Sidebar Navigation
# ======================
menu = st.sidebar.radio(
    "Navigation",
    ["About", "Engineering Philosophy", "Projects", "Technical Stack", "Interests", "Contact"]
)

st.title("Pham Minh Nhut")
st.subheader("Software Engineer | System Builder")

st.divider()

# ======================
# About
# ======================
if menu == "About":
    st.markdown("""
    ### 👋 About Me
    
    I am an IT Engineer focused on building maintainable backend systems 
    and clean Web API architectures.
    
    I value:
    - Clear structure over complexity
    - Maintainability over quick hacks
    - Performance where it matters
    
    Currently exploring deeper system design and scalable backend patterns.
    """)

# ======================
# Philosophy
# ======================
elif menu == "Engineering Philosophy":
    st.markdown("""
    ### 🧠 Engineering Philosophy
    
    Software should be:
    - Readable
    - Scalable
    - Testable
    
    I prefer structured architecture (Clean Architecture mindset)
    and solving real business problems rather than chasing trends.
    """)

# ======================
# Projects
# ======================
elif menu == "Projects":
    st.markdown("### 🚀 Selected Projects")

    st.markdown("""
    #### 🎬 Movie Web Application
    - Built RESTful API using ASP.NET
    - Implemented JWT authentication
    - Designed relational SQL structure
    - Focused on maintainability and separation of concerns
    """)

    st.markdown("""
    #### 📊 Streamlit Dashboard
    - Built interactive data visualization
    - Designed clean UI structure
    - Optimized data loading
    """)

# ======================
# Technical Stack
# ======================
elif menu == "Technical Stack":
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Backend")
        st.markdown("""
        - ASP.NET Web API  
        - C#  
        - JWT Authentication  
        - SQL Server  
        - RESTful Design  
        """)

    with col2:
        st.markdown("### Frontend")
        st.markdown("""
        - JavaScript  
        - HTML/CSS  
        - UI Structure Thinking  
        """)

    with col3:
        st.markdown("### DevOps")
        st.markdown("""
        - Docker  
        - Git  
        - Basic CI/CD  
        """)

# ======================
# Interests
# ======================
elif menu == "Interests":
    st.markdown("""
    ### 📚 Interests
    
    - System Design
    - Automation
    - Backend Optimization
    - Thoughtful UI Design
    """)

# ======================
# Contact
# ======================
elif menu == "Contact":
    st.markdown("""
    ### 📬 Contact
    
    Email: nhuta4@gmail.com  
    LinkedIn: (your link here)  
    GitHub: (your link here)
    """)

st.divider()
st.caption("© 2026 Pham Minh Nhut")