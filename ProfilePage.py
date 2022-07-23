import streamlit as st
import streamlit.components.v1 as stc

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
with open('text.html') as g:
    st.markdown(f'<text>{g.read()}</text>', unsafe_allow_html=True)


st.sidebar.markdown("Profile Page❄️")