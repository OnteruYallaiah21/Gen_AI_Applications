import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Basic Streamlit Setup
st.title("Avinya Solution Powered by Yallaiah Onteru")
st.subheader("Welcome! Enter a website URL to scrape its content and ask questions. 🤖")

# URL input
url = st.text_input("Enter Website URL", value="https://example.com")

# Initialize session state for caching
if 'scraped_content' not in st.session_state:
    st.session_state['scraped_content'] = None
if 'last_url' not in st.session_state:
    st.session_state['last_url'] = None

# Function to scrape website content
def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join([para.text for para in paragraphs])
            return text[:3000]  # Limit to 3000 characters
        else:
            return "❌ Failed to retrieve the website content."
    except Exception as e:
        return f"⚠️ Error occurred: {e}"

# Scrape content only if the URL changes
if url != st.session_state['last_url']:
    st.session_state['last_url'] = url
    st.session_state['scraped_content'] = scrape_website(url)

content = st.session_state['scraped_content']

# Display the content if available
if content:
    st.subheader("🔍 Scraped Content Preview:")
    st.write(content[:500])  # Show the first 500 characters
    st.success("✅ Content successfully retrieved.")
else:
    st.warning("🚨 Please enter a valid website URL.")

# Load a smaller, faster QA model
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Interactive Q&A session
if content:
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Display chat history
    for msg in st.session_state['messages'][-10:]:
        if msg['role'] == 'assistant':
            st.markdown(f'<div class="chat-box assistant">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-box user">{msg["content"]}</div>', unsafe_allow_html=True)

    # User input for asking questions
    question = st.text_input("❓ Ask a question about the content:")

    if question:
        st.session_state['messages'].append({"role": "user", "content": f"User: {question}"})
        with st.spinner("⏳ Generating answer..."):
            result = qa_model(question=question, context=content)
            answer = result.get('answer', '⚠️ Unable to find an answer.')
            st.session_state['messages'].append({"role": "assistant", "content": f"Assistant: {answer}"})
else:
    st.warning("🚨 Scrape a website to enable Q&A.")
