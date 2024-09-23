import streamlit as set

st.title("📧 cold Email Generator")
url_input =  st.text_input("Enter the URL of the company you want to email", value="https://www.metacareers.com/jobs/503684125178318/")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager, I am shriyash", language='markdown' )
