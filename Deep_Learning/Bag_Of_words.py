import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re#support for regular expresdsion
pStemmer=PorterStemmer()
dfMessage=pd.read_csv('D:\Projects\LangchainProjects\DataSets\Reduced_Spam.csv')
dfMessage=dfMessage.drop(dfMessage.columns[0],axis=1)#droping the column 
dfMessage=dfMessage.drop(dfMessage.columns[2],axis=1)#droping the column
dfMessage=dfMessage.rename(columns={'text':'Message'},inplace=False)
print(dfMessage)
#cleaning the data set and preprocessing
corpos=[]
for i in range (0,len(dfMessage)):
    review=re.sub('[^a-zA-Z]',' ',dfMessage['Message'][i])#[^...] =match anything that is NOT
    review=review.split()#converts string to list
    
    review=[pStemmer.stem(word) for word in review if not word in stopwords.words('english')]# after removing the stop words from the sentenses the stemming process would be applied i.e root word
    review=' '.join(review)
    corpos.append(review)
#print(corpos[1])
#create a bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=2500,binary=True,lowercase=True)
X=cv.fit_transform(corpos)
print(X)
#print(X.shape)