import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_Data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df["species"]=iris.target()
    return df,iris.target_names

df,target_name=load_Data()
model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df["species"])
st.sidebar.title("input features")
sepal_length=st.sidebar.slider("Sepal Leangth",float(df['sepal length(cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width=st.sidebar.slider("Sepal width",float(df['Sepal width(cm)'].min()),float(df['Sepal width (cm)'].max()))
petal_length=st.sidebar.slider("petal length",float(df['petal length(cm)'].min()),float(df['petal length (cm)'].max()))
petal_width=st.sidebar.slider("petal width",float(df['petal width(cm)'].min()),float(df['petal width (cm)'].max()))
input_data=[[sepal_length,sepal_width,petal_length,petal_width]]
prediction=model.predict(input_data)
predicted_species=target_names[prediction[0]] 