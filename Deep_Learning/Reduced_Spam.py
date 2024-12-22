import pandas as pd
dfMessage=pd.read_csv('D:\Projects\LangchainProjects\DataSets\spam_ham_dataset.csv')
dfMessage=dfMessage.iloc[5100:]
dfMessage.to_csv("Reduced_Spam.csv",index=False)