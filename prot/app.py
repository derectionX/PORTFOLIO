import streamlit as st

st.set_page_config(
    page_title="Disha Deshmukh | Portfolio",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("Disha Deshmukh")
st.subheader("Engineering Student | Data Analyst & ML Enthusiast")

st.write(
    """
    I build data-driven applications using Python, Machine Learning, and analytics tools.
    I enjoy working with real-world datasets and transforming data into actionable insights.
    """
)

st.divider()

# ---------------- SKILLS ----------------
st.header("🛠 Skills")

st.write("""
- **Programming & Data:** Python, Pandas, NumPy  
- **Machine Learning:** Scikit-learn (Regression, Random Forest)  
- **Visualization:** Matplotlib, Seaborn, Power BI, Excel  
- **Web & Tools:** Streamlit, GitHub  
- **Deployment:** Streamlit Cloud, GitHub Pages  
- **Database:** Basic SQL  
""")

st.divider()

# ---------------- PROJECTS ----------------
st.header("📂 Projects")

# 1. Expense Tracking System
st.subheader("💰 Expense Tracking System")
st.write(
    "Web-based expense tracking application built using Python and Streamlit "
    "to record, manage, and analyze daily expenses."
)

col1, col2 = st.columns(2)
with col1:
    st.link_button(
        "🚀 Live App",
        "https://expensetrackingsystembypython-h3fkng2eluor8nesfwqhy4.streamlit.app/"
    )
with col2:
    st.link_button(
        "💻 GitHub Repo",
        "https://github.com/derectionX/expense_tracking_system_by_python"
    )

st.divider()

# 2. Student Performance Analysis
st.subheader("🎓 Student Performance Analysis")
st.write(
    "Machine learning project to analyze and predict student academic performance "
    "using data preprocessing, feature engineering, and model evaluation."
)

st.link_button(
    "💻 GitHub Repo",
    "https://github.com/derectionX/Student-Performance-Analysis"
)

st.divider()

# 3. SuperStore Sales Dashboard (Power BI)
st.subheader("📊 SuperStore Sales Dashboard (Power BI)")
st.write(
    "Interactive Power BI dashboard analyzing sales performance, KPIs, and trends "
    "to support business decision-making."
)

st.link_button(
    "💻 GitHub Repo",
    "https://github.com/derectionX/Dashboad_by_powerbi_forSuperStore"
)

st.divider()

# 4. Hospitality Domain Analysis
st.subheader("🏨 Hospitality Domain Analysis")
st.write(
    "Exploratory data analysis project on hospitality datasets to uncover trends "
    "in bookings, revenue, occupancy rates, and customer behavior."
)

st.link_button(
    "💻 GitHub Repo",
    "https://github.com/derectionX/project_hospitality_analysis"
)

st.divider()

# 5. Excel Sales Dashboard
st.subheader("📈 Excel Sales Dashboard")
st.write(
    "Sales analysis dashboard created using Excel features such as Pivot Tables, "
    "charts, slicers, and data visualization techniques."
)

st.link_button(
    "💻 GitHub Repo",
    "https://github.com/derectionX/Dashboad_by_excal"
)

st.divider()

# ---------------- CONTACT ----------------
st.header("📬 Contact")

st.write(
    """
    📧 **Email:** your-email@gmail.com  
    💻 **GitHub:** https://github.com/derectionX  
    """
)

st.success("Thank you for visiting my portfolio!")
