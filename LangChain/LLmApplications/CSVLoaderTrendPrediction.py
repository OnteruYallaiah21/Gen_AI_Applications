import os
from langchain.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_community.document_loaders import CSVLoader
from langchain_cohere import ChatCohere
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

set_llm_cache(InMemoryCache())
apikey = os.getenv("COHERE_API_KEY")
llmModel = ChatCohere(model='command-r-plus', max_tokens=200, max_retries=1, api_key=apikey)

try:
    filepath = r"D:\Projects\LangchainProjects\DataSets\retail_sales_dataset.csv"
    if os.path.exists(filepath):
        loader = CSVLoader(filepath)
        docLoader = loader.load()

        # Creating the list for saving the row data
        customerMetaData = []

        for doc in docLoader:
            # Check if page_content contains the actual row data (instead of metadata)
            row_data = doc.page_content  # This should be the actual data
            customerMetaData.append(row_data)

        # Check the first row of data
        if len(customerMetaData) > 0:
            print("First row content:", customerMetaData[0])

        # Define the prompt for customer segmentation
        segmentationPrompt = """
        Here I am giving the Transaction data for Retail business,
        segment customer into distinct groups based on their purchasing behavior,
        suggest the personalized marketing strategy.
        Date:
        -CustomerId:{Customer_ID}
        -age:{age}
        -productCategory:{Product_Category}
        -Quantity:{Quantity}
        -Price:{Price}
        -Total Amount:{Total_Amount}
        """
        template = PromptTemplate(input_variables=["Customer_ID", "age", "Product_Category", "Quantity", "Price", "Total_Amount"], template=segmentationPrompt)
        chain = template | llmModel
        customer_Segments = []

        # Parse each row of data and invoke the chain for customer segmentation
        for row in customerMetaData:
            # Assuming row is a string, we'll split and process it into key-value pairs
            row_parts = row.split("\n")
            row_dict = {}
            for part in row_parts:
                key, value = part.split(":", 1)
                row_dict[key.strip()] = value.strip()

            # Use the customer information in the chain
            customerinfo = chain.invoke({
                "Customer_ID": row_dict.get("CustomerID"),
                "age": row_dict.get("Age"),
                "Product_Category": row_dict.get("ProductCategory"),
                "Quantity": row_dict.get("Quantity"),
                "Price": row_dict.get("PriceperUnit"),
                "Total_Amount": row_dict.get("TotalAmount")
            })

            customer_Segments.append(customerinfo)

        # Prepare and invoke the sales trend prediction
        sales_trend_Prompt = """
        Based on the following sales data, predict the sales trend for the next quarter:
        - total sales for the current quarter is :{currentSales}
        - most popular product category:{productCategory}
        - customer segments:{customerSegments}

        Provide the prediction for the next quarter's sales growth or decline.
        """

        # Calculate current sales and top product category
        currentSales = sum(float(row_dict.get("TotalAmount", 0)) for row_dict in customer_Segments)
        top_Product = max(set(row_dict.get("ProductCategory") for row_dict in customer_Segments), key=[row_dict.get("ProductCategory") for row_dict in customer_Segments].count)

        saleschain = PromptTemplate(input_variables=["currentSales", "productCategory", "customerSegments"], template=sales_trend_Prompt) | llmModel
        sales_Chain_Response = saleschain.invoke({
            "currentSales": currentSales,
            "productCategory": top_Product,
            "customerSegments": customer_Segments
        })

        print(f"Sales prediction trend for the next quarter is: \n{sales_Chain_Response}")

    else:
        print(f"The file path does not exist: {filepath}")
except Exception as e:
    print(f"Error while loading the document: {e}")
