import streamlit as st
import pandas as pd
import numpy as np
## title of the application
st.title("Hello Yallaiah")
#display simple text
st.write("this is simple Text")
#create simple data frame
df=pd.DataFrame({"RollNumbers":[1,2,3,4,5],
                "Student Names":["Yallaiah","Mahesh","Khadar","Praneeth","Rayudu"]})
#dispaly the data frame
st.write("here is my Data frame")
st.write(df)
#create a line chaart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)
