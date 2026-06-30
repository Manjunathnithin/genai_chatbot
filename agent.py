from httpx import stream
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

#chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

#sidebar
with st.sidebar:
    st.title("Chatie piee")

    model = st.selectbox(
        "choose Any Model",
        {
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        }
    )
    if st.button("+ New Chat"):
        st.session_state.messages = [
            {
            "role":"system",
            "content":"""
                    you are a generic Ai assistant
            """
            }
        ]


    st.subheader("Recent Chat")
    for chat in reversed(st.session_state.chat_history[-10:]):
        st.write(f".{chat}")

if "messages" not in st.session_state:
    st.session_state.messages = []

    # Show newest messages first
for message in (st.session_state.messages):
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message['content'])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message['content']) 

prompt = st.chat_input("Text the Ai assistant")

if prompt:
    #SAVE QUESTION / CHAT to side bar history with 50 char limit

    st.session_state.chat_history.append(
        prompt[:50]
    )

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
        answer = ""
        stream = client.chat.completions.create(
            model = model,
            messages = st.session_state.messages,
            stream = True
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                
                answer += token
                response_placeholder.write(answer)

    #save assistant response
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )