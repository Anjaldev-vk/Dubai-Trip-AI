from dotenv import load_dotenv

from openai import OpenAI

import streamlit as st
load_dotenv() 


client=OpenAI()

initial_message =[
{"role": "system", "content": "You are a trip planner in dubai.you are expert in dubai tourisms,locations and hotels etc. You are here to help the user plan their trip to dubai.Responce should be 200 or less words"},
        {
            "role": "user",
            "content": "i am planning a vacation to dubai"
        }
]

def get_response_from_llm(messages):
    completion = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=messages
    )
    return completion.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages=initial_message

st.title("Dubai trip assistance app")

for message in st.session_state.messages:
    if message["role"]!="system":
     with st.chat_message(message["role"]):
       st.markdown(message["content"])

user_message=st.chat_input("Enter your message here...")
if user_message:
   new_message={
      "role":"user",
      "content":user_message
   }
   st.session_state.messages.append(new_message)
   with st.chat_message(new_message["role"]):
       st.markdown(new_message["content"])
   response=get_response_from_llm(st.session_state.messages)
   if response:
       response_message={
          "role":"assistant",
          "content":response
        }
       st.session_state.messages.append(response_message)
       with st.chat_message(response_message["role"]):
         st.markdown(response_message["content"])