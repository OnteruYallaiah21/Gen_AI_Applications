import os
from dotenv import load_dotenv
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_openai import ChatOpenAI
load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING-V2"]="true"
llmModel=ChatOpenAI()
print(llmModel)
