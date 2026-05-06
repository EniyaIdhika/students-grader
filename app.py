# # # import streamlit as st
# # # import pandas as pd
# # # import matplotlib.pyplot as plt

# # # st.title("🎓 Student Result Analyzer")

# # # file = st.file_uploader("Upload CSV", type=["csv"])

# # # if file:
# # #     df = pd.read_csv(file)

# # #     st.subheader("📋 Raw Data")
# # #     st.write(df)

# # #     # Calculate average
# # #     df["Average"] = df.iloc[:, 1:].mean(axis=1)

# # #     # Grade function
# # #     def grade(avg):
# # #         if avg >= 90:
# # #             return "A"
# # #         elif avg >= 75:
# # #             return "B"
# # #         elif avg >= 50:
# # #             return "C"
# # #         else:
# # #             return "Fail"

# # #     df["Grade"] = df["Average"].apply(grade)

# # #     st.subheader("✅ Processed Data")
# # #     st.write(df)

# # #     # Topper
# # #     topper = df.loc[df["Average"].idxmax()]
# # #     st.success(f"🏆 Topper: {topper['Name']} ({topper['Average']:.2f})")

# # #     # Bar chart
# # #     fig, ax = plt.subplots()
# # #     ax.bar(df["Name"], df["Average"])
# # #     st.pyplot(fig)

# # #     # Pie chart
# # #     fig2, ax2 = plt.subplots()
# # #     ax2.pie(df["Grade"].value_counts(), labels=df["Grade"].value_counts().index, autopct="%1.1f%%")
# # #     st.pyplot(fig2)

# # #     # Download
# # #     csv = df.to_csv(index=False).encode("utf-8")
# # #     st.download_button("Download Results", csv, "results.csv")

# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # Page config
# # st.set_page_config(page_title="Student Analyzer", layout="wide")

# # # Title
# # st.title("🎓 Student Result Analyzer Dashboard")

# # # Sidebar
# # st.sidebar.header("⚙️ Options")
# # file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# # if file:
# #     df = pd.read_csv(file)

# #     # Calculate average
# #     df["Average"] = df.iloc[:, 1:].mean(axis=1)

# #     # Grade logic
# #     def grade(avg):
# #         if avg >= 90:
# #             return "A"
# #         elif avg >= 75:
# #             return "B"
# #         elif avg >= 50:
# #             return "C"
# #         else:
# #             return "Fail"

# #     df["Grade"] = df["Average"].apply(grade)

# #     # Rank
# #     df["Rank"] = df["Average"].rank(ascending=False)

# #     # 🔹 TOP METRICS
# #     st.subheader("📊 Key Insights")

# #     col1, col2, col3 = st.columns(3)

# #     topper = df.loc[df["Average"].idxmax()]
# #     col1.metric("🏆 Topper", topper["Name"])

# #     col2.metric("📈 Class Average", f"{df['Average'].mean():.2f}")

# #     pass_percent = (df[df["Grade"] != "Fail"].shape[0] / df.shape[0]) * 100
# #     col3.metric("✅ Pass %", f"{pass_percent:.1f}%")

# #     # 🔹 FILTER
# #     st.sidebar.subheader("Filter")
# #     selected_grade = st.sidebar.selectbox("Select Grade", ["All", "A", "B", "C", "Fail"])

# #     if selected_grade != "All":
# #         df = df[df["Grade"] == selected_grade]

# #     # 🔹 TABLE
# #     st.subheader("📋 Student Data")
# #     st.dataframe(df, use_container_width=True)

# #     # 🔹 CHARTS
# #     col4, col5 = st.columns(2)

# #     # Bar Chart
# #     with col4:
# #         st.subheader("📊 Average Marks")
# #         fig, ax = plt.subplots()
# #         ax.bar(df["Name"], df["Average"])
# #         ax.set_xlabel("Students")
# #         ax.set_ylabel("Average")
# #         st.pyplot(fig)

# #     # Pie Chart
# #     with col5:
# #         st.subheader("🥧 Grade Distribution")
# #         grade_counts = df["Grade"].value_counts()
# #         fig2, ax2 = plt.subplots()
# #         ax2.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
# #         st.pyplot(fig2)

# #     # 🔹 DOWNLOAD
# #     csv = df.to_csv(index=False).encode("utf-8")
# #     st.download_button("⬇ Download Results", csv, "results.csv")

# # else:
# #     st.info("👈 Upload a CSV file from the sidebar to get started")


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Page config
# st.set_page_config(page_title="Student Dashboard", layout="wide")

# # ---------- CUSTOM CSS ----------
# st.markdown("""
# <style>
# .card {
#     padding: 20px;
#     border-radius: 15px;
#     background-color: #1f2937;
#     box-shadow: 0 4px 10px rgba(0,0,0,0.3);
#     text-align: center;
# }
# .card h3 {
#     color: #9CA3AF;
# }
# .card h1 {
#     color: #F9FAFB;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------- TITLE ----------
# st.title("📊 Student Performance Dashboard")

# # ---------- SIDEBAR ----------
# st.sidebar.header("⚙️ Controls")
# file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# if file:
#     df = pd.read_csv(file)

#     # ---------- DATA PROCESSING ----------
#     df["Average"] = df.iloc[:, 1:].mean(axis=1)

#     def grade(avg):
#         if avg >= 90:
#             return "A"
#         elif avg >= 75:
#             return "B"
#         elif avg >= 50:
#             return "C"
#         else:
#             return "Fail"

#     df["Grade"] = df["Average"].apply(grade)
#     df["Rank"] = df["Average"].rank(ascending=False)

#     # ---------- KPI CARDS ----------
#     topper = df.loc[df["Average"].idxmax()]
#     avg_class = df["Average"].mean()
#     pass_percent = (df[df["Grade"] != "Fail"].shape[0] / df.shape[0]) * 100

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.markdown(f"""
#         <div class="card">
#             <h3>🏆 Topper</h3>
#             <h1>{topper['Name']}</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         st.markdown(f"""
#         <div class="card">
#             <h3>📈 Class Avg</h3>
#             <h1>{avg_class:.2f}</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     with col3:
#         st.markdown(f"""
#         <div class="card">
#             <h3>✅ Pass %</h3>
#             <h1>{pass_percent:.1f}%</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     # ---------- FILTER ----------
#     st.sidebar.subheader("Filter")
#     grade_filter = st.sidebar.selectbox("Select Grade", ["All", "A", "B", "C", "Fail"])

#     if grade_filter != "All":
#         df = df[df["Grade"] == grade_filter]

#     # ---------- TABLE ----------
#     st.subheader("📋 Student Data")
#     st.dataframe(df, use_container_width=True)

#     # ---------- CHARTS ----------
#     col4, col5 = st.columns(2)

#     with col4:
#         st.subheader("📊 Average Marks")
#         fig = px.bar(df, x="Name", y="Average", color="Average")
#         st.plotly_chart(fig, use_container_width=True)

#     with col5:
#         st.subheader("🥧 Grade Distribution")
#         fig2 = px.pie(df, names="Grade")
#         st.plotly_chart(fig2, use_container_width=True)

#     # ---------- DOWNLOAD ----------
#     csv = df.to_csv(index=False).encode("utf-8")
#     st.download_button("⬇ Download Results", csv, "results.csv")

# else:
#     st.info("👈 Upload a CSV file to start")


import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Student SaaS Dashboard", layout="wide")

# ---------- CUSTOM CSS (Premium UI) ----------
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #020617;
}

/* Glass Cards */
.card {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    transition: 0.3s;
    text-align: center;
}
.card:hover {
    transform: scale(1.05);
}

/* Titles */
h1, h2, h3 {
    color: white;
}

body, p, span, label {
    color: #b5b5f4 !important;
}

[data-testid="stSidebar"] * {
    color: #b5b5f4 !important;
}

input, textarea, select {
    color: black!important;
}

/* Metric values */
.metric {
    font-size: 30px;
    font-weight: bold;
    color: #90bdf4;
}

/* Buttons */
.stDownloadButton button {
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
# ---------- HEADER ----------
st.markdown("## 🚀 Student Performance SaaS Dashboard")

# ---------- SIDEBAR ----------
st.sidebar.title("📊 Dashboard Controls")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    # ---------- DATA PROCESS ----------
    df["Average"] = df.iloc[:, 1:].mean(axis=1)

    def grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    df["Grade"] = df["Average"].apply(grade)
    df["Rank"] = df["Average"].rank(ascending=False)

    # ---------- KPI CARDS ----------
    topper = df.loc[df["Average"].idxmax()]
    avg_class = df["Average"].mean()
    pass_percent = (df[df["Grade"] != "Fail"].shape[0] / df.shape[0]) * 100

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
    <div class="card">
        <h3>🏆 Topper</h3>
        <div class="metric">{topper['Name']}</div>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div class="card">
        <h3>📈 Class Average</h3>
        <div class="metric">{avg_class:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class="card">
        <h3>✅ Pass Rate</h3>
        <div class="metric">{pass_percent:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- FILTER ----------
    st.sidebar.subheader("🎯 Filter")
    grade_filter = st.sidebar.selectbox("Select Grade", ["All", "A", "B", "C", "Fail"])

    if grade_filter != "All":
        df = df[df["Grade"] == grade_filter]

    # ---------- SEARCH ----------
    search = st.text_input("🔍 Search Student")
    if search:
        df = df[df["Name"].str.contains(search, case=False)]

    # ---------- DATA TABLE ----------
    st.markdown("### 📋 Student Data")
    st.dataframe(df, use_container_width=True)

    # ---------- CHARTS ----------
    col4, col5 = st.columns(2)

    with col4:
        st.markdown("### 📊 Performance")
        fig = px.bar(df, x="Name", y="Average",
                     color="Average",
                     color_continuous_scale="blues")
        st.plotly_chart(fig, use_container_width=True)

    with col5:
        st.markdown("### 🥧 Grade Distribution")
        fig2 = px.pie(df, names="Grade", hole=0.4)
        st.plotly_chart(fig2, use_container_width=True)

    # ---------- DOWNLOAD ----------
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Export Data", csv, "results.csv")

    # ---------- FOOTER ----------
    st.markdown("---")

else:
    st.info("👈 Upload a CSV file to begin")