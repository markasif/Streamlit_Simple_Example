import streamlit as st
import pandas as pd
import numpy as np

st.title("hello fucking ninjaaaa")
st.write("im a data scientist")

df = pd.DataFrame({"Number of workers":[45,3,234,134],
                   "Role of Worker":["junior developer","Manager","Workers","cleaner"]})
st.write("this is the data of company")
st.write(df)

chart_data =pd.DataFrame(np.random.randn(20,3), columns=["a","b","c"])
st.line_chart(chart_data)