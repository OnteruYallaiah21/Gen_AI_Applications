import os
from langchain.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
set_llm_cache(InMemoryCache())
apikey=os.getenv("COHERE_API_KEY")
llm_model=ChatCohere(model='command-r-plus',max_tokens=200,max_retries=1,temperature=0.7)
def genarate_Email_Response(claimNumber,customerName,claimStatus):
    try:
        template=PromptTemplate.from_template("Dear {customerName} your claim with policy number  Numer is {claimNumber}  is cuurentluy in {claimStatus} state once the status the policy is changed we will update you")
        if not claimNumber or not customerName or not claimStatus:
            raise ValueError("all parametrs (claimNumber,customerName,claimStatus) is avlid ")
        prompt=template.format(customerName=customerName,claimNumber=claimNumber,claimStatus=claimStatus)
        response=llm_model.invoke(prompt)
        return response
    except Exception as e:
        return f"error :{str(e)}"
  
#genarating the response
cName="Yallaiah"
customerNumber="AXTR3453"
cStatus="Approved"
resposne=genarate_Email_Response(customerNumber,customerNumber,cStatus)
outputParser=StrOutputParser()
finalEmailResponse=outputParser.parse(resposne)
print(f"the email resposnse is \n{finalEmailResponse}")



    
    
    
    
