import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_core.output_parsers import StrOutputParser
try:
    set_llm_cache(InMemoryCache())
    load_dotenv()
    os.environ['OPENAI_API_KEY']=os.getenv('OPEN_AI_KEY_P')
    os.environ['LANGCHAIN_TRACINF_V2']='true'
    llm_model=ChatOpenAI(model='gpt-4o',max_retries=1,max_tokens=50)
    messages=[SystemMessage(content='Translate the following message in to telugu langauge'),
            HumanMessage(content="Hai how are you")]
    #result=llm_model.invoke(messages)
    #print(result)
    parser=StrOutputParser()
    #here i am making the chain of actions 
    chain= llm_model |parser
    response=chain.invoke(messages)
    print(response)
except Exception as e:
    print(f'the Exception that occur is =>{e}')


'''
1.many of the applications you build with langchain will contain multiple steps with
  multiple invocations of llm callsand these are going to more com[plex
2. we need to inspect the llm applications inside your chain or agent by using the
    Langsmit
'''