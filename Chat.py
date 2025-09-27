import streamlit as st
from dotenv import load_dotenv
import os

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# ----------------------------
# Load environment variables (optional)
# ----------------------------
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Friendly Q&A Chatbot"

# ----------------------------
# Prompt Template
# ----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly and helpful assistant."),
        ("user", "Question: {question}")
    ]
)

# ----------------------------
# Function to generate response
# ----------------------------
def generate_response(question, backend, engine, temperature, max_tokens, api_key=None):
    if backend == "OpenAI":
        if not api_key:
            raise ValueError("OpenAI API Key is required for OpenAI backend.")
        llm = ChatOpenAI(
            model=engine,
            temperature=temperature,
            max_tokens=max_tokens,
            api_key=api_key
        )
    elif backend == "Ollama":
        llm = Ollama(
            model=engine,
            temperature=temperature,
            num_predict=max_tokens
        )
    else:
        raise ValueError("Unsupported backend.")

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"question": question})

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Friendly AI Chat", page_icon="🤖", layout="centered")
st.title("💬 Friendly Q&A Chatbot")

# Sidebar settings
st.sidebar.title("⚙️ Settings")
backend = st.sidebar.selectbox("Select backend", ["OpenAI", "Ollama"])

api_key = None
if backend == "OpenAI":
    api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    engine = st.sidebar.selectbox(
        "Select OpenAI model",
        ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"]
    )
else:
    engine = st.sidebar.selectbox(
        "Select Ollama model",
        ["gemma:2b", "llama2:latest"]
    )

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 150)

st.write("🤖 Ask me anything! (Responses will appear below)")

# Chat history container
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    try:
        # Save user message
        st.session_state.chat_history.append(("You", user_input))

        # Generate AI response
        response = generate_response(user_input, backend, engine, temperature, max_tokens, api_key)
        st.session_state.chat_history.append(("AI", response))

        # Clear input
        st.session_state.input_text = ""

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Display chat history in a friendly format
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**AI:** {message}")
