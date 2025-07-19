from PIL import Image
from dotenv import load_dotenv
load_dotenv()

import  os 
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question,image):
    if question!="" :
        response =model.generate_content([question,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini 1.5 Flash", page_icon=":robot_face:")
st.header("Gemini Image to Text Application")
input = st.text_input("Input prompt",key="input")
upload_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="image")

image = ""

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", width=300)

submit = st.button("Tell me about this image")

if submit:
    response = get_gemini_response(input, image)
    st.subheader('The response is .....')
    st.write(response)