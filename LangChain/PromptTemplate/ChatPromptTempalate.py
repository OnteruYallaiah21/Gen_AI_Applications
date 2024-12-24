from langchain_core.prompts import  ChatPromptTemplate
messages=[("system","You are helpful system to Resolve the student Isuues"),
          "user","Tell me about how to learn the {Technology} Tutorials"]
promptTemplate=ChatPromptTemplate(messages)
response=promptTemplate.invoke({"Technology":"Genrative AI"})
print(f"The response from the langchain is \n{response}")