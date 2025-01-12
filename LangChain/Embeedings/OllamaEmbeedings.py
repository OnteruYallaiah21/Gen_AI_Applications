import os
from langchain.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import OllamaEmbeddings

try:
    set_llm_cache(InMemoryCache)  # Set the LLM cache

    def document_Converter(string):
        return Document(page_content=string)  # Convert string to Document object

    def driver_function(question, list_Documents):
        embeeding_Model = OllamaEmbeddings(model='gemma2:2b')
        # For splitting the Document content we have to use the recursive Text Splitter
        spilit_Doc = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
        # Convert the entire document into a list of page_content Documents
        list_doc = spilit_Doc.split_documents([list_Documents])
        db = Chroma.from_documents(list_doc, embeeding_Model)
        query_result = db.similarity_search(question)
        return query_result  # Return the similarity search result

    passage = '''
    Yallaiah Mom name is Bangaramma.
    Yallaiah Father Name is Kotaiah.
    Yallaiah Sister Name is Avinys
    Yallaiah Favarate sport is Kabaddi
    Yallaiah Favrate dish is Pappu
    '''
    
    # Convert the passage into a Document
    document_Conversion = document_Converter(passage)

    # Define the question
    question = 'who is mother of Yallaiah'

    # Call driver_function with both the question and the document
    result = driver_function(question, document_Conversion)
    print(f"The similarity search result is: {result}")

except Exception as e:
    print(f"the exception is \n{e}")
