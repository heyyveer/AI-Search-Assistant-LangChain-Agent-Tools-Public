import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_youdotcom import YouSearchTool
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import HumanMessage

import uuid

load_dotenv()

st.set_page_config(
    page_title="AI Search Assistant",
    page_icon="🤖",
)

st.title("🤖 AI Search Assistant")

# Create a unique thread for this browser session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())


@st.cache_resource
def load_agent():
    search = YouSearchTool()

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
    )

    memory = MemorySaver()

    agent = create_agent(
        model=llm,
        tools=[search],
        system_prompt="You are an AI assistant that can search the web.",
        checkpointer=memory,
    )

    return agent


agent = load_agent()

config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}

# -------------------------
# Display previous messages
# -------------------------

try:
    state = agent.get_state(config)

    if state.values:
        messages = state.values["messages"]

        for msg in messages:

            if msg.type == "human":
                with st.chat_message("user"):
                    st.markdown(msg.content)

            elif msg.type == "ai":
                with st.chat_message("assistant"):
                    st.markdown(msg.content)

except Exception:
    pass


# -------------------------
# Chat Input
# -------------------------

if prompt := st.chat_input("Ask me anything..."):

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            response = agent.invoke(
                {
                    "messages": [
                        HumanMessage(content=prompt)
                    ]
                },
                config=config,
            )

            answer = response["messages"][-1].content

            st.markdown(answer)
