import streamlit as st
from agent import run_agent

st.title("AI Research Assistant")

topic = st.text_input("Enter topic")

if st.button("Research"):

    with st.spinner("Thinking..."):
        result = run_agent(topic)

    st.write(result)