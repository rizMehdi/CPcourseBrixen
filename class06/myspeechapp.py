#! python3
from googletrans import Translator
from gtts import gTTS 
import streamlit as st
  

st.write("hello")

tts1=gTTS(text='hello world')
tts1.save("audio.mp3")

audio_file = open("audio.mp3", "rb")
audio_data = audio_file.read()

st.markdown(f"## Your audio:")
st.audio(audio_file, format="audio/mp3", start_time=0)

st.download_button(label="Download audio file", data=audio_file, file_name='youraudio.mp3',mime='audio/mp3')
