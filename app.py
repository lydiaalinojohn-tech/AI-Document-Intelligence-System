from utils.gemini_chat import ask_gemini
import streamlit as st
from utils.pdf_reader import extract_text

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("📂 AI Research Assistant")
st.sidebar.write("Upload PDFs and ask questions.")

st.title("🤖 AI Research Assistant")

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    full_text = ""

    for file in uploaded_files:

        st.success(f"Uploaded: {file.name}")

        text = extract_text(file)

        full_text += text + "\n"

    st.subheader("Extracted Text")

    st.text_area(
        "PDF Content",
        full_text,
        height=300
    )

    question = st.text_input(
        "Ask something about this PDF"
    )


if st.button("Ask Gemini"):

    if question.strip() == "":
        st.warning("Please type a question.")
    else:

        with st.spinner("Gemini is thinking..."):

            answer = ask_gemini(question, full_text)

        st.subheader("Gemini Answer")

        st.success(answer)