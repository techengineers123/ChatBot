import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Chat With Bot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

# Create an instance of the model
llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-pro',
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# Create a prompt
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a chatbot"),
        ("human","Question:{question}")
    ]
)

# Create body of the webpage
st.title("🤖 Chat With Your AI Assistant")
st.markdown("### Engage in a friendly conversation and get instant responses!")
input_text = st.text_input("What's on your mind?", placeholder="Type your question here...", help="Ask anything!")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser   
  
if input_text:
    response = (chain.invoke({'question':input_text}))
    st.markdown("### 🤖 Bot's Response:")
    st.write(response)
else:
     st.markdown("#### Go ahead, ask a question above to start the conversation!")

# Create footer
st.markdown("---")
st.markdown("💡 _Powered by Google Generative AI & LangChain Framework_")