
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Student SaaS Dashboard",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

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

/* General Text */
body, p, span, label {
    color: #b5b5f4 !important;
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: #b5b5f4 !important;
}

/* Input Text */
input, textarea, select {
    color: black !important;
}

/* Metric Values */
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
    border: none;
}

.stDownloadButton button:hover {
    transform: scale(1.03);
    opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown("## 🚀 Student Performance SaaS Dashboard")

# ---------------- SIDEBAR ----------------

st.sidebar.title("📊 Dashboard Controls")

files = st.sidebar.file_uploader(
    "Upload Class CSV Files",
    type=["csv"],
    accept_multiple_files=True
)

# ---------------- MAIN APP ----------------

if files:

    class_data = {}

    # ---------- PROCESS EACH FILE ----------

    for file in files:

        df = pd.read_csv(file)

        # Average
        df["Average"] = df.iloc[:, 1:].mean(axis=1)

        # Grade Logic
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

        # Rank
        df["Rank"] = df["Average"].rank(
            ascending=False
        )

        # Store Data
        class_name = file.name.replace(".csv", "")

        class_data[class_name] = df

    # ---------------- COMPARISON ----------------

    comparison = []

    for class_name, df in class_data.items():

        avg_marks = df["Average"].mean()

        pass_percent = (
            df[df["Grade"] != "Fail"].shape[0]
            / df.shape[0]
        ) * 100

        topper = df.loc[
            df["Average"].idxmax()
        ]["Name"]

        comparison.append({
            "Class": class_name,
            "Average Marks": round(avg_marks, 2),
            "Pass %": round(pass_percent, 2),
            "Topper": topper
        })

    comparison_df = pd.DataFrame(comparison)

    # ---------------- KPI SECTION ----------------

    best_class = comparison_df.loc[
        comparison_df["Average Marks"].idxmax()
    ]["Class"]

    avg_all_classes = comparison_df[
        "Average Marks"
    ].mean()

    overall_pass = comparison_df[
        "Pass %"
    ].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>🏆 Best Class</h3>
            <div class="metric">{best_class}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <h3>📈 Overall Average</h3>
            <div class="metric">
                {avg_all_classes:.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <h3>✅ Overall Pass %</h3>
            <div class="metric">
                {overall_pass:.1f}%
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- CLASS COMPARISON ----------------

    st.markdown("## 📊 Class Comparison")

    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    # ---------------- COMPARISON CHART ----------------

    fig_compare = px.bar(
        comparison_df,
        x="Class",
        y="Average Marks",
        color="Average Marks",
        color_continuous_scale="blues",
        title="Class Performance Comparison"
    )

    st.plotly_chart(
        fig_compare,
        use_container_width=True
    )

    # ---------------- INSIGHTS ----------------

    st.markdown("## 🧠 Insights")

    weak_class = comparison_df.loc[
        comparison_df["Average Marks"].idxmin()
    ]["Class"]

    st.warning(
        f"⚠️ Class needing improvement: {weak_class}"
    )

    st.success(
        f"🌟 Best performing class: {best_class}"
    )

    # ---------------- EACH CLASS DETAILS ----------------

    for class_name, df in class_data.items():

        st.markdown(f"---")
        st.markdown(f"# 📘 {class_name}")

        # ---------- SEARCH ----------

        search = st.text_input(
            f"🔍 Search Student in {class_name}",
            key=class_name
        )

        filtered_df = df.copy()

        if search:
            filtered_df = filtered_df[
                filtered_df["Name"].str.contains(
                    search,
                    case=False
                )
            ]

        # ---------- FILTER ----------

        grade_filter = st.selectbox(
            f"🎯 Filter Grade - {class_name}",
            ["All", "A", "B", "C", "Fail"],
            key=f"filter_{class_name}"
        )

        if grade_filter != "All":
            filtered_df = filtered_df[
                filtered_df["Grade"] == grade_filter
            ]

        # ---------- TABLE ----------

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

        # ---------- TOPPER ----------

        topper = df.loc[
            df["Average"].idxmax()
        ]

        st.info(
            f"🏆 Topper: {topper['Name']} "
            f"({topper['Average']:.2f})"
        )

        # ---------- CHARTS ----------

        col4, col5 = st.columns(2)

        # Bar Chart
        with col4:

            fig1 = px.bar(
                filtered_df,
                x="Name",
                y="Average",
                color="Average",
                color_continuous_scale="blues",
                title=f"{class_name} Performance"
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

        # Pie Chart
        with col5:

            fig2 = px.pie(
                filtered_df,
                names="Grade",
                hole=0.4,
                title=f"{class_name} Grade Distribution"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        # ---------- DOWNLOAD ----------

        csv = filtered_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            f"⬇ Export {class_name} Results",
            csv,
            f"{class_name}_results.csv"
        )

else:

    st.info(
        "👈 Upload one or more CSV files "
        "from the sidebar to begin"
    )