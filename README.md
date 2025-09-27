# 💬 Friendly Q&A Chatbot (Ollama + OpenAI)

## Introduction
Welcome to the **Friendly Q&A Chatbot**, a versatile AI-powered chatbot built using **LangChain**, **Ollama**, and **OpenAI**.  
This application allows users to interact with AI models either **locally** through Ollama or **via OpenAI API**, providing a **friendly, conversational experience** with customizable settings for temperature, response length, and model selection.  

---

## Problem Statement
Many users need a conversational assistant to answer questions, summarize information, or provide guidance. Traditional cloud-based AI chatbots may expose sensitive data or require constant internet access.  

This project addresses these challenges by providing:

- **Local AI inference** via Ollama for privacy and offline usage.
- **Cloud AI access** via OpenAI for high-quality responses.
- **Interactive and friendly chat interface**.

**Illustration of the problem:**  
![Problem Illustration](images/chatbot-best-practices.webp)  
*Example showing how the chatbot helps users get answers safely and efficiently.*

---

## Features
- Chat with **OpenAI models** (`gpt-4o`, `gpt-4-turbo`, `gpt-4`, `gpt-3.5-turbo`)  
- Chat with **local Ollama models** (`llama2:latest`, `gemma:2b`)  
- Friendly, chat-like interface with **conversation history**  
- Adjustable **temperature** and **response length**  
- **Combined interface** to switch between OpenAI and Ollama  
- Easy integration of **new AI models**  

---

## Technologies Used
- **Python 3.10+**  
- **Streamlit** – interactive web interface  
- **LangChain** – orchestrating AI prompts and chains  
- **Ollama** – local AI inference  
- **OpenAI API** – cloud AI inference  
- **Markdown & Session State** – for chat formatting  

---

## Project Structure
