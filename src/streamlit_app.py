import streamlit as st

from rag_chain import generate_answer


## =========================================================
## PAGE CONFIG
## =========================================================

st.set_page_config(
    page_title="Finance & Investment RAG Chatbot",
    page_icon="💰",
    layout="wide"
)


## =========================================================
## CUSTOM CSS
## =========================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stChatMessage {
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 10px;
}

.title {
    font-size: 40px;
    font-weight: bold;
    color: #00C897;
}

.subtitle {
    font-size: 18px;
    color: #BBBBBB;
}

</style>
""", unsafe_allow_html=True)


## =========================================================
## HEADER
## =========================================================

st.markdown(
    "<div class='title'>💰 Finance & Investment RAG Chatbot</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Ask your finance and investment questions</div>",
    unsafe_allow_html=True
)

st.divider()


## =========================================================
## SESSION STATE
## =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


## =========================================================
## SIMPLE SIDEBAR
## =========================================================

with st.sidebar:

    st.title("💬 Chat Options")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.rerun()


## =========================================================
## DISPLAY CHAT HISTORY
## =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


## =========================================================
## USER INPUT
## =========================================================

user_input = st.chat_input(
    "Ask your finance question..."
)


## =========================================================
## CHAT LOGIC
## =========================================================

if user_input:

    ## Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    ## Display user message
    with st.chat_message("user"):

        st.markdown(user_input)

    ## Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = generate_answer(user_input)

            st.markdown(response)

    ## Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )