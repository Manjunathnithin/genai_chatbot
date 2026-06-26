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
        st.session_state.message = []



    


if "message" not in st.session_state:
    st.session_state.message = []

    
user_prompt = st.text_area(
    "Enter your prompt here:",
    placeholder="Ask me anything...",

)

if st.button("generate response"):
    if user_prompt:
        st.session_state.message.append(
            {
                "role": "user",
                "content": user_prompt,
            }
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.message
        )

        answer = response.choices[0].message.content
        st.session_state.message.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )
    else:
        st.warning("Please enter a prompt")



# Show newest messages first
for message in reversed(st.session_state.message):
    if message["role"] == "user":
        st.write(f"User: {message['content']}")
    elif message["role"] == "assistant":
        st.write(f"Ai: {message['content']}") 