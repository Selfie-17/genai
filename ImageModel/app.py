from dotenv import  load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini 1.5 Flash", page_icon=":robot_face:")
st.header("Gemini | Aplication")
input = st.text_input("Ask a question to Gemini 1.5 Flash", placeholder="Type your question here...",key="input")
submit = st.button("Ask the question")

if input:
    response = get_gemini_response(input)
    st.subheader("Response from Gemini 1.5 Flash")
    st.write(response)