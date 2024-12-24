import os
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# Get the API key from the environment variable
apikey = os.environ.get("COHERE_API_KEY")
print(apikey)  # Check if the API key is being fetched correctly

# Initialize the ChatCohere model with the appropriate parameters
llmmodel = ChatCohere(model="command-r-plus", temperature=0.7, max_tokens=100, api_key=apikey)

# Prepare the messages for translation
messages = [
    SystemMessage("Translate the text into Telugu."),
    HumanMessage("Hai hello, doing this is Yallesh from Avinys Tech Solutions."),
]

# Create an output parser
parser = StrOutputParser()

# Invoke the model with the messages
final_output = llmmodel.invoke(messages)

# Parse the output
string_output = parser.invoke(final_output)

# Print the final output
print(string_output)
