from langchain_core.prompts import MessagesPlaceholder
prompt=MessagesPlaceholder("history",optional=True)# with out optional=true it can genarate the key error
print(prompt.format_messages())# retruns the Empty list