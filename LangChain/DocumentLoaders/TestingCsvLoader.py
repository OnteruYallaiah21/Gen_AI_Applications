import os
from langchain_community.document_loaders import CSVLoader

# Path to the CSV file
filepath = r"D:\Projects\LangchainProjects\DataSets\retail_sales_dataset.csv"

# Check if the file exists
if os.path.exists(filepath):
    # Load the CSV file
    loader = CSVLoader(filepath)
    docLoader = loader.load()
    
    # Create the list for saving metadata
    customerMetaData = []
    for doc in docLoader:
        row = doc.metadata  # Extract metadata for each row
        customerMetaData.append(row)

    # Print metadata of the first row (as before)
    if len(customerMetaData) > 0:
        print("First row metadata:", customerMetaData[0])
    else:
        print("No metadata loaded from the CSV file.")
    
    # Print actual content of the first row
    if len(docLoader) > 0:
        print("First row content:", docLoader[0].page_content)  # Check page_content for actual data
    else:
        print("No content loaded from the CSV file.")
