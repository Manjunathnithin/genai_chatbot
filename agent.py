from groq import Groq
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#we use this to have title, pagelayout and assist sidebar
st.set_page_config(
    page_title="Chatie piee",
    layout="wide",
    initial_sidebar_state="expanded",
)

#sidebar
with st.sidebar:
    st.title("Chatie piee")
    if st.button("+ New Chat"):
        st.session_state.messages = []



    


if "messages" not in st.session_state:
    st.session_state.messages = []

    # Show newest messages first
for message in reversed(st.session_state.messages):
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message['content'])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message['content']) 

prompt = st.chat_input("Text the Ai assistant")

if prompt:
    
    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    #accept prompt and write it to LLM
    with st.chat_message("user"):
        st.write(prompt);

    with st.chat_message("assistant"):
        response_placeholder = st.empty()

        response = client.chat.completions.create(
            model ="llama-3.3-70b-versatile",
            messages = st.session_state.messages
        )

        answer = response.choices[0].message.content
        
        response_placeholder.write(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )