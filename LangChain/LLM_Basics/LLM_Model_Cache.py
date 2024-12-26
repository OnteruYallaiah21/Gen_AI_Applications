import os
import time
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_cohere import ChatCohere
set_llm_cache(InMemoryCache())
apiKey=os.getenv("COHERE_API_KEY")
llm_Model=ChatCohere(model='command-r-plus',max_tokens=100,max_retries=1,api_key=apiKey)
startTime=time.time()
response=llm_Model.invoke("Tell me About the GEN AI FEATURE as in statistics boom in feature")
endTime=time.time()
print(f"the reposnse is \n{response}\n Time taken for response=> {endTime-startTime} ")
startTime=time.time()
response=llm_Model.invoke('Tell me About the GEN AI FEATURE as in statistics boom in feature')
endTime=time.time()
print(f"the reposnse in second time \n{response}\n Time taken for response=> {endTime-startTime} ")
#by using the cache technique we can reduce the numn=ber of calls and resposnse time also
