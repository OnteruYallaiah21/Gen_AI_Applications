from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
try:
    filePath='D:\Projects\LangchainProjects\DataSets\Insurance.pdf'
    pdfloader=PyPDFLoader(filePath)
    content=pdfloader.load()
    ##print(f'the pdf content is {content}')
    #how to recursively split the text in to
    textsplitters=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50) 
    finalconent=textsplitters.split_documents(content)
    print(type(finalconent))
    print(finalconent[0])
    print(finalconent[1])

except FileNotFoundError:
    print(f'the file path is not found in the {filePath}')
except Exception as customError:
    print(f'the error is {customError}')