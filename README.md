# Text Summarization & Question-Answering Web App

An NLP web application that combines automatic text summarization with extractive question answering, allowing users to process long text, ask questions about it, and obtain concise summaries.

## Demo

<p align="center">
<img width="1000" height="600" alt="Text-Summarization" src="https://github.com/user-attachments/assets/9bb41e9b-4012-4f80-b10e-f9a82c7b14ec" />
</p>

## Overview

The project demonstrates an end-to-end NLP pipeline built with Python and Hugging Face transformer models.

Users can provide a block of text and either:

- Ask a question to extract a relevant answer from the text.
- Generate a concise summary of the provided content.

The application was deployed as an interactive **Streamlit** web app.

## Key Features

- Question Answering using a RoBERTa model fine-tuned on SQuAD2.
- Text summarization using a Hugging Face transformer model.
- Text preprocessing and inference pipeline in Python.
- Interactive Streamlit interface.
- End-to-end integration of multiple NLP models in a single application.

## Models

### Question Answering

**Model:** `deepset/roberta-base-squad2`

A RoBERTa-based model fine-tuned on the SQuAD2 dataset for extractive question answering.

### Summarization

**Model:** `Falconsai/text_summarization`

A Hugging Face transformer model used to generate concise summaries from longer passages.

## How It Works

```text
Input Text
    │
    ├──────────────► Question + Text
    │                    │
    │                    ▼
    │               RoBERTa QA
    │                    │
    │                    ▼
    │               Extracted Answer
    │
    └──────────────► Summarization
                         │
                         ▼
                    Concise Summary
```

## Tech Stack

- Python
- Hugging Face Transformers
- RoBERTa
- T5-based summarization
- Streamlit

## What I Learned

This project provided hands-on experience with transformer-based NLP workflows, model inference, text preprocessing, pipeline integration, and deploying an NLP application through Streamlit.

## Running the Application

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run the Streamlit application:

```bash
streamlit run app.py
```

The exact entry-point filename may vary depending on the repository structure.
