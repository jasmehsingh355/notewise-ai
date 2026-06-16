import streamlit as st

st.title("📚 NoteWise AI")
st.write("Convert lecture recordings into study notes")

uploaded_file = st.file_uploader(
    "Upload Lecture Audio",
    type=["mp3", "wav"]
)

if uploaded_file:

    st.success("Audio uploaded successfully!")

    st.subheader("📝 Generated Notes")

    st.write("""
    • Topic: Supply Chain Management

    • Key Concepts:
      - Procurement
      - Logistics
      - Inventory Management

    • Important Definition:
      Supply Chain refers to the movement of goods and services from supplier to customer.
    """)

    st.subheader("📄 Lecture Summary")

    st.write("""
    This lecture explained the fundamentals of supply chain management,
    procurement processes, logistics operations, and inventory control.
    """)

    st.subheader("🧠 Flashcards")

    st.info("""
    Q: What is Procurement?

    A: The process of obtaining goods and services.
    """)

    st.subheader("❓ Quiz")

    answer = st.radio(
        "What is the first stage of a supply chain?",
        ["Marketing", "Procurement", "Accounting"]
    )

    if st.button("Check Answer"):
        if answer == "Procurement":
            st.success("Correct!")
        else:
            st.error("Incorrect. The answer is Procurement.")
