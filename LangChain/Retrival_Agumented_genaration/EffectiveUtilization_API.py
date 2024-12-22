import os
import time
from langchain.globals import set_llm_cache
from langchain_community.llms import OpenAI
from langchain_community.cache import InMemoryCache
from langchain_cohere import ChatCohere
try:
    apikey = os.environ.get("COHERE_API_KEY")
    openaikey=os.getenv('OPEN_API_KEY_S')
    #print(f'the open api keys is {openaikey}')
    llm_model=OpenAI(model='gpt-3.5-turbo',max_tokens=1,temperature=0.7)
    llmmodel = ChatCohere(model="command-r-plus", temperature=0.7, max_tokens=10, api_key=apikey)

    set_llm_cache(InMemoryCache())
    start_time=time.time()
    response=llmmodel.predict('who is narendra modi')
    end_time=time.time()
    print(f'the first response from the llm model is {response} and Excecution time{end_time-start_time}' )
    start_time=time.time()
    response=llmmodel.predict('who is narendra modi')
    end_time=time.time()
    print(f'the Second response from the llm model is {response} and Excecution time{end_time-start_time}' )
except Exception as e:
    print(f"the exception is {e}")

    