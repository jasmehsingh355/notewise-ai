import streamlit as st

st.title("📚 NoteWise AI")

st.write("Convert lecture recordings into study notes")

uploaded_file = st.file_uploader(
    "Upload Lecture Audio",
    type=["mp3", "wav"]
)

if uploaded_file:
    st.success("Audio uploaded successfully!")

    st.subheader("Generated Notes")

    st.write("""
    • Topic: Supply Chain Management

    • Key Concepts:
    - Procurement
    - Logistics
    - Inventory Management
    """)

    st.subheader("Lecture Summary")

    st.write("""
    This lecture discussed supply chain management
    and its importance in business operations.
    """)
