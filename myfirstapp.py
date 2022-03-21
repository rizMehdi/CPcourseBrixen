import streamlit as st
st.header("hello world")
title = st.text_input('Gimme a movie title', '<enter a movie title here in EN', max_chars=7)
st.write('The current movie title is', title)

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
