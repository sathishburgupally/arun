import streamlit as st
import streamlit as st
import pandas as pd
from joblib import load
model =  load("model1.joblib")
# Streamlit inputs
st.title("Bank loan elegibility check ")

# Input for marital status
m = st.radio("Enter marital status:", options=["Married", "Unmarried"])

# Input for income
i = st.number_input("Enter your income:", min_value=0, step=1000)

# Input for credit history
c = st.selectbox("Credit history:", options=["Good", "Bad"])

d1 = {"married" :[m],"income":[i],"Credit_History":[c]}
df = pd.DataFrame(d1)
df["Credit_History"].replace({"Good":1,"Bad":0},inplace=True)


df1 =df[["Credit_History"]]
df1
if st.button("predict"):
    if model.predict(df1):
        st.write("You are eligible")
    else : 
        st.write("Sorry you are not eligible")
