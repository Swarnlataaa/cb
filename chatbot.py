import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

st.title("Child rights chatbot")

user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input:
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50,  # Adjust this as needed
            stop=None,  # You can specify stop words if needed
            temperature=0.7,  # Adjust temperature for creativity
        )
        bot_response = response.choices[0].text
        st.text("Bot:" + bot_response)
    else:
        st.text("Bot: Please enter a question.")
