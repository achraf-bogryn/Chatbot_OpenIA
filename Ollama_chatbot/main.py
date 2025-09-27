import streamlit as st
from dotenv import load_dotenv
import os

# LangChain imports
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# ----------------------------
# Load environment variables (optional)
# ----------------------------
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"

# ----------------------------
# Prompt Template
# ----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# ----------------------------
# Function to generate response
# ----------------------------
def generate_response(question, engine, temperature, max_tokens):
    llm = Ollama(
        model=engine,
        temperature=temperature,
        num_predict=max_tokens   # ✅ use num_predict instead of max_tokens
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"question": question})


# ----------------------------
# Streamlit UI
# ----------------------------
st.title("💬 Enhanced Q&A Chatbot with Ollama")

# Sidebar for settings
st.sidebar.title("⚙️ Settings")

engine = st.sidebar.selectbox(
    "Select Ollama model",
    ["gemma:2b", "llama2:latest"]  # 👈 make sure these are installed via `ollama pull`
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 150)

# Main interface
st.write("🤖 Go ahead and ask me any question:")

user_input = st.text_input("You:")

if user_input:
    try:
        response = generate_response(user_input, engine, temperature, max_tokens)
        st.success(response)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
