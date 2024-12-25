from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
message=[("system","you are helpful assistant to the student"),
          MessagesPlaceholder("history"),("human","{question}")]
promptValue=ChatPromptTemplate.from_messages(message)
questions={"history":[("human","whare R.ummadivaram is located"),
                      ("ai","The R.ummadivaram village is located in pullacheruvu mandal")],
           "question":"where the pullalacheruvu is located"
           }
response=promptValue.invoke(questions)
parser=StrOutputParser()
print(f"the prompt value is {response.to_messages()}")