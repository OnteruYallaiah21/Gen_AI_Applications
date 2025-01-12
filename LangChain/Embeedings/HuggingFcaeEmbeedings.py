import os
from langchain_huggingface import HuggingFaceEmbeddings
os.environ['HF_TOKEN']='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'
embeeding=HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
text="this is Text  document"
queryResult=embeeding.embed_query(text)
print(f"the length of embeeding result is {len(queryResult)} \n {queryResult}and ")