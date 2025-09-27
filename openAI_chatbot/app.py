import streamlit as st
from dotenv import load_dotenv
import os

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# ----------------------------
# Load environment variables
# ----------------------------
load_dotenv()

# LangSmith Tracking (optional)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With OpenAI"

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
def generate_response(question, api_key, engine, temperature, max_tokens):
    # Initialize the model
    llm = ChatOpenAI(
        model=engine,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=api_key
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("💬 Enhanced Q&A Chatbot with OpenAI")

# Sidebar for settings
st.sidebar.title("⚙️ Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

engine = st.sidebar.selectbox(
    "Select the OpenAI model",
    ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"]
)

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=500, value=150)

# Main interface
st.write("🤖 Go ahead and ask me any question:")

user_input = st.text_input("You:")

if user_input:
    if api_key:
        try:
            response = generate_response(user_input, api_key, engine, temperature, max_tokens)
            st.success(response)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("🔑 Please enter your OpenAI API Key in the sidebar.")
