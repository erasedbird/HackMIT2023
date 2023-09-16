import streamlit as st
from audiorecorder import audiorecorder


st.markdown("<h1 style='text-align: center;'>Tell us how you feel</h1>", unsafe_allow_html=True)

st.write("<h3 style='text-align: center; color: lightSeaGreen;'>we'll generate the insights</h3>", unsafe_allow_html=True)

audio = audiorecorder("Click to record", "Click to stop recording")


if not audio.empty():
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("audio.wav", format="wav")

    # To get audio properties, use pydub AudioSegment properties:
    st.text_area(label="Output", 
                value=f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds", 
                height=300)
