import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]   
})

st.write("Here is the DataFrame:")
st.write(df)

st.title("Streamlit Text Input")
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")
age = st.slider("Select your age:", 0, 100, 25)

st.write(f"You are {age} years old.")
options = ["Python", "JavaScript", "Java", "C++"]
choice = st.selectbox("Select your favorite programming language:", options)

st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello, {name}!")
data = {
   "Name": ["John", "Alice", "Bob"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"] 
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)