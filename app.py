import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student SaaS Dashboard", layout="wide")

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

st.markdown("## 🚀 Student Performance SaaS Dashboard")

st.sidebar.title("📊 Dashboard Controls")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

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

    st.sidebar.subheader("🎯 Filter")
    grade_filter = st.sidebar.selectbox("Select Grade", ["All", "A", "B", "C", "Fail"])

    if grade_filter != "All":
        df = df[df["Grade"] == grade_filter]

    search = st.text_input("🔍 Search Student")
    if search:
        df = df[df["Name"].str.contains(search, case=False)]

    st.markdown("### 📋 Student Data")
    st.dataframe(df, use_container_width=True)

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

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Export Data", csv, "results.csv")

    st.markdown("---")

else:
    st.info("👈 Upload a CSV file to begin")