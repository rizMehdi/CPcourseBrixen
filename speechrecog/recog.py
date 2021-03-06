
import speech_recognition as sr
import streamlit as st
import requests   


st.write(st.secrets["my_token"])


r = sr.Recognizer()

#AUDIO_FILE = "sample_audio_short.wav"   #mp3 files are not supported
#AUDIO_FILE = "sample_audio_long.wav"    #these files are in files-section of Class06 folder, on MS Teams.
#https://github.com/rizMehdi/CPcourseBrixen/blob/main/speechrecog/sample_audio_long.wav

AUDIO_FILE=st.file_uploader("upload your audio file")
if AUDIO_FILE is not None:
  st.audio(AUDIO_FILE, format="audio/wav")
  with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file   
  recognised_text= r.recognize_google(audio)
  st.text('the text recognized from the audio seems to be: ')
  st.text( recognised_text)
