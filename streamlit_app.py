import requests

import streamlit as st
import requests  # <-- Add this line to fix the NameError
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Streamlit UI
st.title("Intelligent Agent Query Interface")

# Input field for user query
user_query = st.text_input("Enter your query:")

if st.button("Submit Query"):
    # Send the query to the FastAPI agent endpoint
    response = requests.post("http://localhost:8000/agent_action", json={"query": user_query})
    
    # Display the response
    if response.status_code == 200:
        result = response.json()
        st.write(f"Action Taken: {result['action']}")
        st.write(f"Result: {result['result']}")
    else:
        st.write("Failed to get a response from the agent.")
