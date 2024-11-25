from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set required environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["OPENAI_API_KEY"] = 'Copy your OpenAI API KEY'

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Initialize LLama2 via Ollama or ChatOpenAI
llm = ChatOpenAI(model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

## Streamlit Framework: Enhanced Design
st.set_page_config(
    page_title="EliteThinker AI 🌟",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom Header
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ff9800; /* Orange-Gold Color */
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
    }
    .user-input {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
        font-size: 1.2rem;
    }
    .response {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-header">EliteThinker AI 🌟</div>', unsafe_allow_html=True)

# User Input Section
st.subheader("Ask EliteThinker AI Anything!")
input_text = st.text_input("Type your question below", placeholder="E.g., What is Artificial Intelligence?", key="user_input")

# Display LLM Output with Styling
if input_text:
    with st.spinner("Thinking... 🤔"):
        response = chain.invoke({"question": input_text})
        st.markdown('<div class="response">{}</div>'.format(response), unsafe_allow_html=True)

# Sidebar for Additional Info
st.sidebar.header("About EliteThinker AI 🌟")
st.sidebar.info(
    """
    - EliteThinker AI is powered by **LangChain** and **GPT-4**.
    - It’s designed to answer your questions with precision and clarity.
    - For more information, visit [LangChain](https://www.langchain.com/).
    """
)

st.sidebar.header("How it Works")
st.sidebar.write(
    """
    1. **Type a Question:** Enter any question in the input box.
    2. **View the Response:** EliteThinker AI generates an insightful response.
    3. **Powered by AI:** Uses GPT-4 for smart and reliable responses.
    """
)
