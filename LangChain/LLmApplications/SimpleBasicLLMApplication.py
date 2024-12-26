import os 
import traceback
from langchain.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
try:
    set_llm_cache(InMemoryCache())
    LANGCHAIN_TRACING_V2=True
    LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
    LANGCHAIN_API_KEY="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"
    LANGCHAIN_PROJECT="YalleshLangchainApplications"
    apikey=os.getenv("COHERE_API_KEY")
    llmModel=ChatCohere(model="command-r-plus",max_tokens=100,max_retries=1)
    promptTemplate1=PromptTemplate.from_template("Tell me the primiminister of the {country}")
    promptTemplate=promptTemplate1.format(country="India")
    parser=StrOutputParser()
    response=llmModel.invoke(promptTemplate)
    outputResponse=parser.parse(response)
    print(f"the Response from the llm model is {outputResponse}")
except Exception as e:
    print(f"the exception is occurd in the process is {e}")
    traceback.print_exc()