import streamlit as st
from transformers import pipeline

# Load models
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

# App title
st.title("🧠 NLP Web App")
st.write("Choose between **Question Answering** or **Text Summarization**.")

# Sidebar selection
mode = st.sidebar.radio("Select Mode", ["Question Answering", "Text Summarization"])

# --- Question Answering ---
if mode == "Question Answering":
    st.subheader("Question Answering")
    
    context = st.text_area("Enter your paragraph/context:", height=200)
    question = st.text_input("Enter your question:")
    
    if st.button("Get Answer"):
        if context.strip() and question.strip():
            result = qa_pipeline(question=question, context=context)
            st.success(f"**Answer:** {result['answer']}")
        else:
            st.warning("Please provide both a context and a question.")

# --- Text Summarization ---
elif mode == "Text Summarization":
    st.subheader("Text Summarization")
    
    text = st.text_area("Enter text to summarize:", height=200)
    
    if st.button("Summarize"):
        if text.strip():
            result = summarizer(text, max_length=130, min_length=30, do_sample=False)
            st.success(f"**Summary:** {result[0]['summary_text']}")
        else:
            st.warning("Please provide text to summarize.")
