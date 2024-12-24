import os
import traceback
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
try:
    load_dotenv()
    os.environ["Langchain_Tracing_v2"]='true'
    apikey=os.getenv("COHERE_API_KEY")
    llm_model=ChatCohere(model='command-r-plus',max_tokens=100,api_key=apikey,temperature=0.7)
    tempalte="Can you tell me How prepare the dish in style of {Style_of_Dish}"
    prompt_template=ChatPromptTemplate([("system",tempalte),("user","{DishName}")])
    response=prompt_template.invoke({"Style_of_Dish":"Iran","DishName":"Biryani"})
    #if we print the above output we get response the like ai bot genarated style for developing the user
    #user defined styel we can use the output parser
    outputresponse=response.to_messages()
    print(f"the message from the llm model is \n{outputresponse}") 
    
    
except Exception as e:
    print(f"the exception is {e}")
    traceback.print_exc()
    