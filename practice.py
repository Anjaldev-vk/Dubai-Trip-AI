import streamlit as st

st.title("hello anjal")
name = st.text_input("Enter your name")
if st.button("Say Hello"):
    st.write(f"Hello {repr(name)}, Welcome to the Upcode")  

