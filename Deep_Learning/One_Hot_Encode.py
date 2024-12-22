import pandas as pd
from sklearn.preprocessing import OneHotEncoder

Data={
      'rollNumbers':[1,2,3,4],
      'Names':['Yallaiah','Khadar','Rayudu','Mahesh']
      }
print(Data)
df=pd.DataFrame(Data) 
print(f"originl Data frame is \n{df}")
#encodes intilization
encode=OneHotEncoder(sparse_output=False)
NamesEncodeing=encode.fit_transform(df[['Names']])
print(f"the Names are encodes is =>{NamesEncodeing}")
Names_encoding=pd.DataFrame(NamesEncodeing,columns=encode.categories_[0])
print(f"the dataframe in encode form is \n{Names_encoding}")