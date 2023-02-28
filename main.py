import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/peter.png")

with col2:
    st.title("Peter Chay")
    content = """Hello, my name is Peter. I am a Lead QE Engineer at Mersive Technologies and I am currently learning 
    python so that I cam build out tools and create automated tests. Welcome to my portfolio page, below you will see 
    the applications I have built."""

    st.info(content)