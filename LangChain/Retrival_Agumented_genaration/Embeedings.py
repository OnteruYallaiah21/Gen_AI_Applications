import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv #LOAD ALL ENVIRONMENTAL VARIBALES 
try:
    os.environ['OPENAI_API_KEY']=os.getenv('OPEN_AI_KEY_P')
    #coverting the text in to vector
    embeddings=OpenAIEmbeddings(model='text-embedding-3-large')
    text='this is text about the embeeding for the open ai'
    query_result=embeddings.embed_query(text)
    print(f'{query_result}/n type is  {type(query_result)}/n the length=>{len(query_result)}/n the emding=>{query_result[0]}')
except Exception as e:
     print(f"the exception is {e}")