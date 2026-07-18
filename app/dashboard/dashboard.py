from api_client import( 
    get_latest_metrics,
    get_recent_metrics
    )

import streamlit as st
from streamlit_autorefresh import st_autorefresh

st_autorefresh(
    interval=5000,
    key="refresh"
)

import requests


st.title("SENTINEL")
metrics = get_latest_metrics()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="CPU",
        value=f"{metrics['cpu_percent']}%"
    )

with col2:
    st.metric(
        label="MEMORY",
        value=f"{metrics['memory_percent']}%"
    )
def format_bytes(num_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(num_bytes)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024


col3, col4 = st.columns(2)

with col3:
    st.metric(
        label="DISK USAGE",
        value=f"{metrics['disk_percent']}%"
    )

with col4:
    st.metric(
        label="MEMORY USED",
        value= format_bytes(metrics["memory_used"])
    )


col5, col6 = st.columns(2)

with col5:
    st.metric(
        "Bytes Sent",
        format_bytes(metrics["bytes_sent"])
    )

with col6:
    st.metric(
        "Bytes Received",
        format_bytes(metrics["bytes_received"])
    )

history = get_recent_metrics()
st.write(len(history))

cpu_history = [metric["cpu_percent"] for metric in history]

st.subheader("CPU Usage History")

st.line_chart(cpu_history)

memory_history = [metric["memory_percent"] for metric in history]

st.subheader("Memory Usage History")
st.line_chart(memory_history)

disk_history = [metric["disk_percent"] for metric in history]

st.subheader("Disk Usage History")
st.line_chart(disk_history)