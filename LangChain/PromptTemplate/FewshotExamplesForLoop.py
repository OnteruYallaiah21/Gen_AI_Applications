from langchain_core.prompts import PromptTemplate
example_Prompt="Translate the follwing text in to Telugu\nQuestion:{input_Text}\nResponse:{Response}"
Examples=[
    {"input_Text":"Hai How are you","Response":"namste ela unnav nuvvu"},
    {"input_Text":"what are doing here","Response":"miru ikkada emi chestunnaru"},
    {"input_Text":"I am here to take my breakfast","Response":"nenu ikkada na yokka udhayam put alpaharam thisukoniki vachanu"}
    
]
for example in Examples:
    formatted_text=example_Prompt.format(**example)
    print(formatted_text)