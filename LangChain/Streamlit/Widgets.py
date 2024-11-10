import streamlit as st
import pandas as pd
st.title("Strealit Text Input")
name=st.text_input("Enter your name")
age=st.slider("select your age:",0,100,25)
st.write(f"you age is {age}")
options=["Python","Java","c++","Scala"]
choise=st.selectbox("choose your favorate langauge:",options)
st.write(f"you selected {choise}")
dfNames=pd.DataFrame({"Name":["Yallaiah","Khadar","Praneeth","Ganesh","Mahesh"],
                 "City":["Milwaukee","Guntur","Iowa","Milwaukee","Kenasas"],
                 "PHONE":[6856898,55252535,52532454,5235353,42443412]})
dfNames.to_csv("SampleStreamLit.csv")
st.write(dfNames)
uploade_file=st.file_uploader("choose csv file",type="csv")
if uploade_file is not None:
    df=pd.read_csv(uploade_file)
    st.write(df)
    
if name:
    st.write(f"Hello   {name} how are you")
