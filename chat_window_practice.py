import streamlit as st

st.title("Chat Window")


with st.chat_message("assistant"):
    st.write("Hello, I am your AI assistant")


with st.chat_message("human"):
    st.markdown("I am planning a vacation to Dubai")


message = st.chat_input("Enter your message")

if message:
    with st.chat_message("human"):
        st.markdown(message)
