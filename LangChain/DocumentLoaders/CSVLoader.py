import os
from langchain_community.document_loaders import CSVLoader
try:
    filepath=r"D:\Projects\LangchainProjects\DataSets\retail_sales_dataset.csv"
    if os.path.exists(filepath):
        loader=CSVLoader(file_path=filepath)
        docLoader=loader.load()
        #print(f"In the csv file the data is the \n{docLoader}")
        print(docLoader[0].page_content[:100])
        print(f"the meta data of the document is {docLoader[0].metadata}")
    else:
        print(f"the file is not exists in the specified path {filepath}")
except Exception as e:
    print(f"the error while loading the file is {e}")