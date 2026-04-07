
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Operational Intelligence Assistant",
    layout="centered"
)

# Title and description
st.title("AI‑Powered Operational Intelligence Assistant")
st.caption("MVP Prototype – File Failure Analysis & Recommendation")

st.markdown("---")

# Section 1: Input
st.header("1. Upload or Paste Failure Details")

failure_text = st.text_area(
    "Paste error log / failure message",
    height=200,
    placeholder="Example: File rejected due to UTF-16 encoding instead of UTF-8..."
)

partner = st.selectbox(
    "Select Partner",
    ["Partner A", "Partner B", "Partner C", "Other"]
)

file_type = st.selectbox(
    "File Type",
    ["EDI", "CSV", "XML", "JSON"]
)

analyze = st.button("Analyze Failure")

st.markdown("---")

# Section 2: Analysis Output
if analyze and failure_text.strip():
    st.header("2. AI Analysis Output")

    st.subheader("Identified Root Cause")
    st.success(
        "File encoding mismatch – received UTF‑16 instead of required UTF‑8"
    )

    st.subheader("Impact Assessment")
    st.write(
        "• Auto‑processing failed\n"
        "• Manual intervention required\n"
        "• SLA at risk"
    )

    st.subheader("Recommended Corrective Action")
    st.info(
        "Request partner to switch file encoding to UTF‑8 and resend the file."
    )

    st.subheader("Preventive Recommendation")
    st.write(
        "Enable pre‑validation encoding checks for all inbound files from this partner."
    )

    st.markdown("---")

    # Section 3: Conversational Follow-Up
    st.header("3. Conversational Follow‑Up")

    question = st.text_input("Ask a follow‑up question")

    if question:
        st.write("AI Response:")
        st.write(
            "This issue has occurred multiple times previously with the same partner "
            "due to incorrect encoding configuration. Enforcing UTF‑8 validation at "
            "source or during pre‑ingestion will prevent recurrence."
        )

# Footer
st.markdown("---")
st.caption(
    "This MVP prototype demonstrates the end‑to‑end workflow of the AI‑Powered "
    "Operational Intelligence Assistant. AI outputs are simulated for academic "
    "demonstration purposes."
)
