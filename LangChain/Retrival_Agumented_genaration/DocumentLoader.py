import os
from langchain_community.document_loaders import TextLoader,PyPDFLoader,WebBaseLoader

file_path='D:\Projects\LangchainProjects\DataSets\Insurance.pdf'
text_path='D:\Projects\LangchainProjects\DataSets\Insurance.txt'
if not os.path.exists(file_path):
    print(f'the file does not exist at {file_path}')
else:
    print(f'the file is exist at {file_path}')
try:
 pdf_loader=PyPDFLoader(file_path)
 text_loader=TextLoader(text_path)
 Text_Doc=text_loader.load()
 pdf_doc=pdf_loader.load()
 print(f'the pdf document is =>{text_loader}')
 print(f'the type of document is {type(text_loader)}')
except FileNotFoundError:
    print(f'The file not found ')
except Exception as yerraor:
    print(f'the errror is caused by the {yerraor}')
#here we are taking the laoding the webbased loader
webased_do=WebBaseLoader(web_path=('https://content.naic.org/sites/default/files/inline-files/State%20Licensing%20Handbook%20-%20Complete%20and%20Final.pdf'))
web_doc=webased_do.load(webased_do)
print(f'the web based loader is file is {web_doc}')