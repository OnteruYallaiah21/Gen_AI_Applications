import os
from langchain.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
set_llm_cache(InMemoryCache())
apikey=os.getenv("COHERE_API_KEY")
llm_model=ChatCohere(model="command-r-plus",max_tokens=200,max_retries=1,api_key=apikey)
def groupMessages(questions):
    try:
        if questions:
            tempalte=ChatPromptTemplate([("ai","you are helpful ai bot for the genaral questions for providing the Suggestions in steps wise "),
                                         MessagesPlaceholder("claims")])
            claimQuestions=[HumanMessage(content=claim) for claim in questions ]
            final_Template=tempalte.invoke({"claims":claimQuestions})
            #print(f"the final template is {final_Template}")
            response=llm_model.invoke(final_Template)
            return response
    except Exception as e:
      return f"The Error is {str(e)}"
    
questions=["Tell about Defferent Insurance Opportunities in the india",
           "which is Best Insurance among all",
           "what benifits do i get if i take the insurance policy"]
finalresponse=groupMessages(questions)
parser=StrOutputParser()
print(f"the final response is \n{parser.parse(finalresponse)}")