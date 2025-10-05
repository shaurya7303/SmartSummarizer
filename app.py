import streamlit as st
from transformers import pipeline
from newspaper import Article


st.set_page_config(page_title="SmartSummarizer", page_icon="📰", layout="centered")
st.title(" SmartSummarizer ")
st.markdown("Turn long news articles or blog posts into **3 concise sentences** using AI.")


@st.cache_resource
def load_model():
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return summarizer

with st.spinner("Loading summarization model"):
    summarizer = load_model()
st.success("Model loaded successfully ")

option = st.radio("Choose input type:", ("Paste Text", "Paste Article URL"))

user_input = ""
if option == "Paste Text":
    user_input = st.text_area(" Paste your text here:", height=250)
else:
    url = st.text_input(" Paste the article/blog URL:")
    if st.button("Fetch Article"):
        if url.strip():
            try:
                with st.spinner("Fetching article"):
                    article = Article(url)
                    article.download()
                    article.parse()
                    user_input = article.text
                    st.success("Article fetched successfully!")
                    st.text_area("Extracted Article:", value=user_input, height=250)
            except Exception as e:
                st.error(f"Failed to fetch article: {e}")
        else:
            st.warning("Please enter a valid URL.")


if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Summarizing"):
            summary = summarizer(
                user_input, max_length=150, min_length=40, do_sample=False
            )[0]["summary_text"]

        st.subheader(" Summary:")
        st.write(summary)
        st.balloons()
    else:
        st.warning(" Please provide text or URL content to summarize.")

st.caption("Built with  Shaurya")
