import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

from ensemble import ensemble_retriever_from_docs
from full_chain import create_full_chain, ask_question
from langchain.retrievers import EnsembleRetriever


st.set_page_config(page_title="VNGCloud AI Assistant")
st.title("VNGCloud AI Assistant")


def show_ui(qa, prompt_to_user="How may I help you?"):
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": prompt_to_user}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            content = ""
            with st.spinner("Thinking..."):
                content = ""
                placeholder = st.empty()
                for msg in qa.stream(
                    {"question": prompt},
                    config={"configurable": {"session_id": "foo"}}
                ):
                    if content == "":
                        content += "💭 THINKING...\n\n\n"

                    if msg.content.strip() == "</think>":
                        content += "\n\n\n💬 ANSWERING...\n"
                        continue

                    content += msg.content
                    placeholder.markdown(content)
        message = {"role": "assistant", "content": content}
        st.session_state.messages.append(message)


@st.cache_resource
def get_retriever() -> EnsembleRetriever:
    embeddings: HuggingFaceEmbeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
    )

    return ensemble_retriever_from_docs(embeddings=embeddings)


def get_chain(openai_api_key=None, huggingfacehub_api_token=None):
    ensemble_retriever = get_retriever()
    chain = create_full_chain(ensemble_retriever,
                              chat_memory=StreamlitChatMessageHistory(key="langchain_messages"))
    return chain


def get_secret_or_input(secret_key, secret_name, info_link=None):
    if secret_key in st.secrets:
        st.write("Found %s secret" % secret_key)
        secret_value = st.secrets[secret_key]
    else:
        st.write(f"Please provide your {secret_name}")
        secret_value = st.text_input(secret_name, key=f"input_{secret_key}", type="password")
        if secret_value:
            st.session_state[secret_key] = secret_value
        if info_link:
            st.markdown(f"[Get an {secret_name}]({info_link})")
    return secret_value


def run():
    ready = True

    if ready:
        chain = get_chain(openai_api_key="", huggingfacehub_api_token="")
        st.subheader("Dịch vụ hỗ trợ khách hàng tự động được cung cấp bởi VNGCloud")
        show_ui(chain, "Xin chào, mình là Orin. Mình là trợ lí ảo nhằm giải đáp các thắc mắc của khách hàng về các dịch vụ của VNGCloud. Bạn có câu hỏi gì không?")
    else:
        st.stop()


run()
