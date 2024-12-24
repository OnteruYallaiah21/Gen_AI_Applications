import os
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_cohere import ChatCohere
from langchain_core.output_parsers import StrOutputParser
apikey=os.getenv('COHERE_API_KEY')
set_llm_cache(InMemoryCache)
llmmodel=ChatCohere(model="command-r-plus",temperature=0.7,max_tokens=100,api_key=apikey)
response=llmmodel.invoke('can you tell how to prepare biryani in in iran style')
parses=StrOutputParser()
print(f"the llm model resposne is \n{parses.parse(response)}")

