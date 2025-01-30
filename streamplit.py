import streamlit as st

st.header ("This is git Demo Webpage!")

name=st.text_input("Enter Your Name:")
button = st.button("Submit")

if button:
    st.info("Your Name is {name}")
    