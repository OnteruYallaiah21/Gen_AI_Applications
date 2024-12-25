from langchain_core.prompts import MessagesPlaceholder
prompt=MessagesPlaceholder("history",optional=True)
print(prompt.format_messages())