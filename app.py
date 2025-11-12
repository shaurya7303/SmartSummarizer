import streamlit as st
from transformers import pipeline
from newspaper import Article

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="SmartSum",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #111827, #1f2937, #0f172a);
        color: #f3f4f6;
        font-family: 'Poppins', sans-serif;
    }
    .main-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 4px 30px rgba(0,0,0,0.2);
        margin-top: 40px;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #3b82f6, #06b6d4);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 10px rgba(59,130,246,0.5);
    }
    div.row-widget.stRadio > div {
        justify-content: center;
    }
    h1, h2, h3, h4 {
        text-align: center;
        color: #f9fafb;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1>📰 SmartSummarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#9ca3af;'>Turn long news articles or blogs into <b>3 concise sentences</b> using AI </p>", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "article_text" not in st.session_state:
    st.session_state.article_text = ""

# ---------- MODEL LOADING ----------
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

with st.spinner("⚙️ Loading summarization model..."):
    summarizer = load_model()
st.success("Model loaded successfully!")

# ---------- INPUT ----------
option = st.radio("Choose Input Type:", ("Paste Text", " Paste Article URL"))

if option == " Paste Text":
    st.session_state.article_text = st.text_area(" Paste your text here:", height=250)

else:
    url = st.text_input("Paste the article/blog URL:")
    if st.button(" Fetch Article"):
        if url.strip():
            try:
                with st.spinner(" Fetching article..."):
                    article = Article(url)
                    article.download()
                    article.parse()
                    st.session_state.article_text = article.text
                    st.success("✅ Article fetched successfully!")
            except Exception as e:
                st.error(f" Failed to fetch article: {e}")
        else:
            st.warning(" Please enter a valid URL.")
    if st.session_state.article_text:
        st.text_area("Extracted Article:", value=st.session_state.article_text, height=250)

# ---------- SUMMARIZE ----------
if st.button(" Summarize"):
    text = st.session_state.article_text.strip()
    if text:
        with st.spinner(" Generating summary..."):
            try:
                summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]["summary_text"]
                st.markdown("<h3> Summary:</h3>", unsafe_allow_html=True)
                st.success(summary)
                st.balloons()
                st.info(f"Word Count: {len(summary.split())}")
            except Exception as e:
                st.error(f" An error occurred: {e}")
    else:
        st.warning(" Please provide text or fetch article first.")

# ---------- FOOTER ----------
st.markdown("""
    <hr style="border:1px solid #374151; margin-top:50px;">
    <p style='text-align:center; color:#9ca3af;'>
        Built by <b>Shaurya</b> 
    </p>
""", unsafe_allow_html=True)
