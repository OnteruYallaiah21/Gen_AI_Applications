import os
from langchain.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

set_llm_cache(InMemoryCache())
apikey=os.getenv("COHERE_API_KEY")
llm_Model=ChatCohere(model="command-r-plus",max_tokens=200,max_retries=1,api_key=apikey)
def chatInsurance_Agent(useQuery,uName,cateGerory):
    try:
        if useQuery and uName and cateGerory:
            tempalate=ChatPromptTemplate([("system","You are helpfull AI bot for recomendations and Suggestions and queries"),
                                                        ("user","hello,my name is {uName} and I ahave Question about the {cateGerory}"),
                                                        ("ai","hello {uName} how can I assiste with your {cateGerory} today"),
                                                        ("user","{useQuery} and Can you recommend any youtube or any website links for reference ")])
            response=tempalate.invoke({"uName":uName,"cateGerory":cateGerory,"useQuery":useQuery})
            llm_Response=llm_Model.invoke(response)
            #print(f"response is \n{llm_Response}")
            return llm_Response
        else:
            message="the Details are not matching can You provide all details  and Reach me out"
            print(f"the Details are not matching can You provide all details  and Reach me out")
            return message
    except Exception as e:
        return f" the error is {str(e)}"

userName="Yallaiah"
category="life insurance"
userQuery="What is coverage limit for the Lic Life Insurance"

response=chatInsurance_Agent(userQuery,userName,category) 
parser=StrOutputParser() 
print(parser.parse(response)) 
