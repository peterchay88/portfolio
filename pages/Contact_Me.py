import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Please Enter your Email Address: ")
    message = st.text_area("Please enter message below")
    button = st.form_submit_button("Submit")

    if button:
        message = message

