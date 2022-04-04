import streamlit as st
import json, requests 
from googletrans import Translator

translator = Translator()


keyword= st.text_input('hi i am your translation chatbot. what you want to translate? ','')
if keyword !='':
  keyword_it = translator.translate(keyword, src='en', dest='it')
  if keyword == 'nothing':
    print('ok. bye !')
    
st.write(keyword, 'is called', keyword_it.text, 'in italian')
 
