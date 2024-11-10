"""
*propmpt template basically formats  the user input, and that is passed to large language model
*if we provide few examples to llm model that type of technique is called the few shoting
*a few shot example is constructed from the few shot examples or example selectors
 
"""
from langchain_core.prompts import PromptTemplate


Examples=[{"question":"who is the owner of Avinya solutions",
          "answer":"""Yallaiah onteru is the owner of the Avinys solutions""",},
          {"question":"who is father of the yallaiah onteru",
          "answer":"""Onteru kotaih is the father of the onteru yallaiah""",},
          {"question":"where he was born",
           "answer":"""he was bron and bought in india in pullacheruvu""",}
          ]

example_prompt=PromptTemplate.from_template("Question:{question}\n{answer}")
print(example_prompt.invoke(Examples[0]).to_string())
