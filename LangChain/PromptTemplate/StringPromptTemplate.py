import os
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
set_llm_cache(InMemoryCache)
apikey=os.getenv('COHERE_API_KEY')
llm_model=ChatCohere(model='command-r-puls',temperature=0.7,max_tokens=100,max_tries=1,api_key=apikey)
promptInput=PromptTemplate.from_template('tell about the about the {Culture} ')
response=promptInput.invoke({"Culture":"Hindu"})
parser=StrOutputParser()
finalresponse=parser.parse(response)
print(f"the sting prompt tempalate response is \n{finalresponse} ")


