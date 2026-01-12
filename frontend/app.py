import streamlit as st
import requests

st.title("LLaMA Text Summarizer")

user_input = st.text_area("Enter your text here:")

if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        response = requests.post(
            "http://localhost:8000/summarize/",
            data={"text": user_input}
        )

        if response.status_code == 200:
            summary = response.json()["summary"]
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error(f"Backend error: {response.text}")
