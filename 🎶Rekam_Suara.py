import streamlit as st
from st_custom_components import st_audiorec


st.set_page_config(page_title="Rekam Suara")

st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)

st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)

st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True) 
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  


def audiorec_demo_app():

    
    st.title('Aplikasi Audio Recorder')
    st.markdown('Didamel oleh : '
        '[Pariz Maulana Septiana](https://www.linkedin.com/in/pariz-maulana-septiana/)')
    st.write('\n\n')
 

    wav_audio_data = st_audiorec() 

   
    col_info, col_space = st.columns([0.57, 0.43])
    with col_info:
        st.write('\n') 
        st.write('\n') 
      
    if wav_audio_data is not None:
        
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')


if __name__ == '__main__':
  
    audiorec_demo_app()
