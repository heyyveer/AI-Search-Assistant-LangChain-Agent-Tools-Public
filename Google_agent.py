import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_youdotcom import YouSearchTool

load_dotenv()

st.set_page_config(
    page_title="AI Search Assistant",
    page_icon="🤖",
)

st.title("🤖 AI Search Assistant")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize agent only once
@st.cache_resource
def load_agent():
    search = YouSearchTool()

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
    )

    return create_agent(
        model=llm,
        tools=[search],
        system_prompt="You are an AI assistant that can search the web."
    )

agent = load_agent()

# Display previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            response = agent.invoke(
                {
                    "messages": st.session_state.messages
                }
            )

            answer = response["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )