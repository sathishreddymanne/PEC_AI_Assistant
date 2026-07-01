import streamlit as st
from main import load_rag_chain

st.set_page_config(
    page_title="PEC AI Assistant",
    page_icon="🎓",
    layout="wide"
)

@st.cache_resource
def get_rag_chain():
    return load_rag_chain()

rag_chain = get_rag_chain()

st.title("🎓 Prathyusha Engineering College AI Assistant")
st.write("Ask anything about Prathyusha Engineering College.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = ""

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask your question...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Get response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = rag_chain.invoke(
                {
                    "question": question,
                    "chat_history": st.session_state.chat_history
                }
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.chat_history += (
        f"\nUser: {question}\nAssistant: {answer}"
    )

with st.sidebar:

    st.title("🎓 PEC Chatbot")

    st.write("College Information Assistant")

    st.divider()

    st.write(f"Questions Asked : {len([m for m in st.session_state.messages if m['role']=='user'])}")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.session_state.chat_history = ""
