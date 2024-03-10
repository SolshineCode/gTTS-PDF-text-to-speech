import streamlit as st
from gtts import gTTS 
from io import BytesIO
from PyPDF2 import PdfReader

st.image('OIG3 (4).jpeg', caption='Your host on this PDF-to-Speech adventure!')

x = st.slider('Select the number of pages you wish to transcribe')

uploaded_file = st.file_uploader("Choose a file", "pdf")
if uploaded_file is not None: 
    # creating a pdf reader object
    reader = PdfReader(uploaded_file)
    # printing number of pages in pdf file
    X = len(reader.pages)
    print(X)

    i = 0
    while i <= X and i <= x:
        # getting a specific page from the pdf file
        page = reader.pages[i]
        # extracting text from page
        text = page.extract_text()  
        print("Created text of page", i )
        sound_file = BytesIO()
        tts = gTTS(text, lang='en')
        tts.write_to_fp(sound_file)
        st.audio(sound_file)
        print("Read aloud", i, "pages of", X, "total pages.")
        i = i + 1
    st.write("🎉 That's the whole PDF! Have an awesome day! 🎉")
    

prompt = st.chat_input("Copy/Paste or type in text to have read aloud")
if prompt:
    st.write(prompt)
    with st.popover("✨ Open your text-to-speech from text input ✨"):
        sound_file = BytesIO()
        tts = gTTS(prompt, lang='en')
        tts.write_to_fp(sound_file)
        
        st.audio(sound_file)
