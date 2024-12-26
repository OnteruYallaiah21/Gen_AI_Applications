import os 
import traceback
from fpdf import FPDF
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_cohere import ChatCohere
from langchain_core.output_parsers import StrOutputParser
try:
    #set_llm_cache(InMemoryCache)
    apikey = os.environ.get("COHERE_API_KEY")
    llmmodel = ChatCohere(model="command-r-plus", temperature=0.7, max_tokens=100, api_key=apikey)
    load_dotenv()
    os.environ['langchain_tracing_v2']='true'
    os.environ['OPENAI_API_KEY']=os.getenv('OPEN_AI_KEY_P')
    question="can you tell me  how to prepare the in style of  {style_of_dish}"
    prompt_template=ChatPromptTemplate.from_messages([("system",question),("user","{dishname}")])
    parser=StrOutputParser()
    model_chain=prompt_template | llmmodel | StrOutputParser
    response=model_chain.invoke({"style_of_dish":"iran", "dishname":"chicken Biryani"})
    folderpath="D:\Projects\LangchainProjects\DataSets"
    filename="dishPreaparation"
    save_file(folderpath,filename,response)
    print(f"the Response From Yallaiah Model is \n {response}")
    def save_file(folder_path,filename,Response_message):
        os.mkdir(folder_path,exist_ok=True)
        filepath=os.path.join(folder_path,f"{filename}.pdf")
        pdf=FPDF()
        pdf.set_auto_page_break(auto=True,margin=0.4)
        pdf.add_page()
        pdf.add_font("Arial",size=10)
        for line in Response_message.split("\n"):
            pdf.multi_cell(0,10,line)
        pdf.output(filepath)
        print(f"the file is saved in the file path of {filepath}")
        
except Exception as e:
    print(f"the Exception is {e}")
    traceback.print_exc()
    
'''
1. in this modulle you will laern what is output parser and usage 
2. what is prompttempate
3.how to chain the actions
4.chaching tehnique to save repsonse time api calls to the llm model
'''
