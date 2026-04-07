
import streamlit as st

st.set_page_config(page_title="AI Operational Intelligence Assistant", layout="centered")

st.title("AI‑Powered Operational Intelligence Assistant")
st.caption("MVP Prototype – File Failure Analysis & Recommendation")

st.markdown("---")

# Input section
st.header("1. Upload or Paste Failure Details")
failure_text = st.text_area(
    "Paste error log / failure message",
    height=200,
    placeholder="Example: File rejected due to UTF-16 encoding instead of UTF-8..."
)

partner = st.selectbox("Select Partner", ["Partner A", "Partner B", "Partner C", "Other"])
file_type = st.selectbox("File Type", ["EDI", "CSV", "XML", "JSON"])

analyze = st.button("Analyze Failure")

st.markdown("---")

if analyze and failure_text:
    st.header("2. AI Analysis Output")

    st.subheader("Identified Root Cause")
    st.success("File encoding mismatch – received UTF‑16 instead of required UTF‑8")

    st.subheader("Impact Assessment")
    st.write("• Auto‑processing failed
• Manual intervention required
• SLA at risk")

    st.subheader("Recommended Corrective Action")
    st.info("Request partner to switch file encoding to UTF‑8 and resend file")

    st.subheader("Preventive Recommendation")
    st.write("Enable pre‑validation encoding check for incoming files from this partner")

    st.markdown("---")

    st.header("3. Conversational Follow‑Up")
    q = st.text_input("Ask a follow‑up question")
    if q:
        st.write("AI Response:")
        st.write("This issue has occurred 4 times previously with the same partner due to incorrect encoding configuration.")

st.markdown("---")
st.caption("This prototype demonstrates the MVP workflow and user experience. AI responses are simulated for demonstration purposes.")
