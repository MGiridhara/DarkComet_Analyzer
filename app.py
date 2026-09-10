import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from detector.threat_score import calculate_threat_score

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="DarkComet RAT Behavioral Analyzer",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- AUTO REFRESH ----------------

st_autorefresh(
    interval=10000,  # 10 seconds
    key="dashboard_refresh"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.dashboard-title {
    text-align: center;
    color: #00FF99;
    font-size: 40px;
    font-weight: bold;
    padding-bottom: 10px;
}

.section-title {
    color: #00CCFF;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    "<div class='dashboard-title'>🛡️ DarkComet RAT Behavioral Analyzer</div>",
    unsafe_allow_html=True
)

st.caption(
    f"🕒 Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

st.markdown("---")

# ---------------- SIDEBAR ----------------

st.sidebar.title("Navigation")
st.sidebar.success("Auto Refresh Enabled")
st.sidebar.info("Dashboard updates every 10 seconds")

# ---------------- LOAD DATA ----------------

try:
    data = pd.read_csv("logs/activity_log.csv")
except FileNotFoundError:
    st.error("activity_log.csv not found inside logs folder.")
    st.stop()

data.columns = data.columns.str.strip()

# ---------------- REQUIRED COLUMNS ----------------

required_columns = [
    "process_name",
    "cpu_usage",
    "memory_usage",
    "status"
]

missing = [col for col in required_columns if col not in data.columns]

if missing:
    st.error(f"Missing columns: {missing}")
    st.write("Available columns:", data.columns.tolist())
    st.stop()

# ---------------- THREAT SCORE ----------------

data["threat_score"] = data.apply(
    lambda row: calculate_threat_score(
        row["cpu_usage"],
        row["memory_usage"],
        row["status"]
    ),
    axis=1
)

# ---------------- SEVERITY ----------------

def get_severity(score):
    if score < 30:
        return "LOW"
    elif score < 60:
        return "MEDIUM"
    elif score < 85:
        return "HIGH"
    else:
        return "CRITICAL"

data["severity"] = data["threat_score"].apply(get_severity)

# ---------------- AI ANALYSIS ----------------

def explain_threat(row):

    reasons = []

    if row["cpu_usage"] > 70:
        reasons.append("High CPU usage")

    if row["memory_usage"] > 500:
        reasons.append("High memory consumption")

    if row["status"] != "SAFE":
        reasons.append("Suspicious process behavior")

    if not reasons:
        return "Normal process behavior detected."

    return " | ".join(reasons)

data["ai_analysis"] = data.apply(
    explain_threat,
    axis=1
)

# ---------------- OVERVIEW ----------------

safe_count = len(data[data["status"] == "SAFE"])
threat_count = len(data[data["status"] != "SAFE"])
total_processes = len(data)

avg_score = round(
    data["threat_score"].mean(),
    2
)

# ---------------- KPI DASHBOARD ----------------

st.subheader("📊 Security Overview")

overall_risk = int(data["threat_score"].mean())

st.subheader("🎯 System Risk Level")

st.progress(overall_risk)

st.metric(
    "Current Risk Score",
    f"{overall_risk}%"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Processes", total_processes)
col2.metric("Safe", safe_count)
col3.metric("Threats", threat_count)
col4.metric("Avg Threat Score", avg_score)

st.markdown("---")

# ---------------- CHARTS ----------------

left, right = st.columns(2)

with left:

    st.subheader("🔥 Threat Distribution")

    chart_data = pd.DataFrame(
        {
            "Count": [safe_count, threat_count]
        },
        index=["SAFE", "THREAT"]
    )

    st.bar_chart(chart_data)

with right:

    st.subheader("📈 CPU Usage Trend")

    st.line_chart(data["cpu_usage"])

st.markdown("---")

# ---------------- RECENT PROCESSES ----------------

st.subheader("🖥️ Recent Processes")

st.dataframe(
    data[
        [
            "process_name",
            "cpu_usage",
            "memory_usage",
            "status",
            "threat_score",
            "severity"
        ]
    ].tail(20),
    use_container_width=True
)

# ---------------- THREAT ALERTS ----------------

st.subheader("🚨 Threat Alerts")

suspicious = data[data["status"] != "SAFE"]

if not suspicious.empty:

    st.error(
        f"{len(suspicious)} suspicious process(es) detected"
    )

    st.dataframe(
        suspicious[
            [
                "process_name",
                "cpu_usage",
                "memory_usage",
                "status",
                "threat_score",
                "severity"
            ]
        ],
        use_container_width=True
    )

else:

    st.success(
        "No suspicious activities detected."
    )

# ---------------- CRITICAL THREATS ----------------

critical = data[
    data["severity"] == "CRITICAL"
]

if not critical.empty:

    st.subheader("☠️ Critical Threats")

    st.error(
        f"{len(critical)} critical threat(s) detected"
    )

    st.dataframe(
        critical[
            [
                "process_name",
                "threat_score",
                "severity"
            ]
        ],
        use_container_width=True
    )

# ---------------- TOP THREATS ----------------

st.subheader("⚠️ Top Threat Rankings")

top_threats = data.sort_values(
    by="threat_score",
    ascending=False
).head(10)

st.dataframe(
    top_threats[
        [
            "process_name",
            "status",
            "threat_score",
            "severity"
        ]
    ],
    use_container_width=True
)

# ---------------- AI ANALYSIS PANEL ----------------

st.subheader("🤖 AI Threat Analysis")

selected_process = st.selectbox(
    "Select a Process",
    data["process_name"].unique()
)

selected_row = data[
    data["process_name"] == selected_process
].iloc[0]

st.info(selected_row["ai_analysis"])

col1, col2 = st.columns(2)

col1.metric(
    "Threat Score",
    selected_row["threat_score"]
)

col2.metric(
    "Severity",
    selected_row["severity"]
)

# ---------------- RAW LOGS ----------------

with st.expander("📜 View Full Activity Logs"):

    st.dataframe(
        data,
        use_container_width=True
    )

# ---------------- FOOTER ----------------

st.markdown("---")

st.success(
    "🛡️ DarkComet RAT Behavioral Analyzer Active"
)