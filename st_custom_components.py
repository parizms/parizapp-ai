import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components

def st_audiorec():

   
    parent_dir = os.path.dirname(os.path.abspath(__file__))
   
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    
    raw_audio_data = st_audiorec() 
    wav_bytes = None               


    if isinstance(raw_audio_data, dict): 
        with st.spinner('retrieving audio-recording...'):
            ind, raw_audio_data = zip(*raw_audio_data['arr'].items())
            ind = np.array(ind, dtype=int)  
            raw_audio_data = np.array(raw_audio_data)  
            sorted_ints = raw_audio_data[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            
            wav_bytes = stream.read()

    return wav_bytes