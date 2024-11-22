import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name =st.text_input("Enter your name")

if name: 
    st.write(f"Hello, Mr/Ms {name} Welcome to streamless experience of streamlit")

age = st.slider("Enter your age",0,75,25)
st.write(f"Your age is {age}")

options = ["Bold","Shy","Crazy","Anger","peace"]
choice = st.selectbox("Choose Your Character",options)
st.write(f"Showing My Nature, It is {choice}.")

check= st.checkbox("Click here")
st.write("State of check box",check)
if check : 
    st.write(":smile:"*12)

df = pd.DataFrame({"Name":["usman", "rahul" , "christy", "josph", "mohammed", "varun"],
                   "Games":["football","handball","volleyball","cricket","Rugby","Football"],
                   "Rating: 1-100":[82,46,98,79,83,60]})
st.write(df)

upload_file = st.file_uploader("Upload Your Cv Here...",type="csv")

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)
