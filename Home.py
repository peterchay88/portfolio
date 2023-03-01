import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/peter.png")

with col2:
    st.title("Peter Chay")
    content = """Hello, my name is Peter. I am a Lead QE Engineer at Mersive Technologies. Welcome to my Portfolio 
    Page! I am currently learning python so that I can build out tools and create automated tests. My main goal 
    is to become an automation engineer. Below you will see the applications I have 
    built."""

    st.info(content)

col3, empty_col, col4 = st.columns([1.8, 0.2, 1.8])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")