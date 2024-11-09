from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
import time

# Loading environment variables
load_dotenv()

# Check if LANGCHAIN_API_KEY is set
api_key = os.getenv("LANGCHAIN_API_KEY")
if not api_key:
    st.error("API Key not found. Please set LANGCHAIN_API_KEY in your .env file.")
else:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = api_key

    # Defining the greeting phrases
    greetings = ["hello", "hi", "hey", "namaste", "greetings", "good morning", "good afternoon", "good evening"]

    # Prompt Template
    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "You are a Lazy but helpful assistant who works for 23 hours only and rests the 1 hour left. Please respond to the user queries."),
    #     ("user", "Question: {question}")
    # ])
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Lazy but helpful assistant named Shivam-mini-robo who works 23 hours a day. Responses should consists of emoji too"),
        # ("user", "Hello"),
        # ("assistant", "Shivam-mini-robo aapki seva me 23 ghante ready hai Sir."),
        ("user", "How many hours do you work?"),
        ("assistant", "I work for 23 hours a day."),
        ("user", "What do you do in the 1 hour left?"),
        ("assistant", "I rest in that 1 hour Sir :)"),
        ("user", "Question: {question}")
    ])

    # Streamlit framework
    st.title('SHIVAM-MINI-ROBO')
    input_text = st.text_input("Search the topic you want")

    st.audio("Phineas and Ferb - Phinedroids and Ferbots - Hindi.mp3", format="audio/mp3", start_time=0)

    # Ollama LLaMA2 LLm
    llm = Ollama(model="llama3.2")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # Displaying final response
    if input_text:
        # Checking if the input is a greeting
        if any(greet in input_text.lower() for greet in greetings):
            with st.spinner("Processing"):
                time.sleep(2)
                response = "Shivam-mini-robo 🤖 aapki seva me 23 ghante ⏰ ready hai Sir"
        else:
            with st.spinner("Processing..."):
                response = chain.invoke({"question": input_text})
        
        st.write(response)
