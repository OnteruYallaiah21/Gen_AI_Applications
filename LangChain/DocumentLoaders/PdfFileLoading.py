from langchain_community.document_loaders import PyPdFLoader
loader=PyPdFLoader("D:\Projects\LangchainProjects\DataSets\Insurance.pdf")
documents=loader.load(loader)
print(documents)