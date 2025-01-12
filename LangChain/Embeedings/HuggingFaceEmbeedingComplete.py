import os
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['HF_TOKEN'] = os.getenv('HF_API_KEY')
set_llm_cache(InMemoryCache())

try:
    text_String = '''  

Yallesh is an enthusiastic learner and developer with a keen interest in the field of **Generative AI (Gen AI)** applications. With the rapidly evolving nature of artificial intelligence, Gen AI stands out as a groundbreaking area that holds immense potential in various industries, from content creation to problem-solving in scientific research.

Generative AI refers to systems designed to create content, whether it's text, images, videos, or even music, through models like GANs (Generative Adversarial Networks), transformers, or autoencoders. These AI models are capable of producing new, previously unseen data, closely resembling the data they were trained on. For instance, language models like GPT (Generative Pre-trained Transformers) can write coherent essays or code, while image generation models like DALL·E can create artwork based on textual descriptions.

Yallesh is particularly drawn to how **Generative AI** is transforming industries such as entertainment, healthcare, finance, and marketing. In entertainment, AI-generated music and art are pushing creative boundaries, while in healthcare, Gen AI helps with drug discovery by simulating molecular behavior. Additionally, marketing teams are using AI to generate personalized content and advertisements that resonate more with their target audience.

Yallesh sees vast potential in **Gen AI applications** in automation, enhancing creativity, and improving productivity across sectors. Their passion for this field leads them to actively explore new tools, frameworks, and methods to contribute to the development of **AI-driven solutions** that can shape the future.

In the future, Yallesh aspires to apply their knowledge to solve real-world problems using **Generative AI**, whether by creating innovative AI applications or contributing to research that pushes the boundaries of what’s possible in the field.'''

    doc_Obj = Document(page_content=text_String)
    spliter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=100)
    list_Doc = spliter.split_documents([doc_Obj])
    embeeding = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    vectorDb = FAISS.from_documents(list_Doc, embeeding)
    print(f"the vector db results is {vectorDb}")
    
    query = 'Yallaiah Interested in what'
    query_Serach = vectorDb.similarity_search(query)
    saveLocal=vectorDb.save_local('faiss_index')
    print(query_Serach[0].page_content)
    
except Exception as e:
    print(f"the exception is =>{e}")
