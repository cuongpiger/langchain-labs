import os

from dotenv import load_dotenv
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate

from basic_chain import get_model
from filter import ensemble_retriever_from_docs
from local_loader import load_txt_files
from memory import create_memory_chain
from rag_chain import make_rag_chain


def create_full_chain(retriever, openai_api_key=None, chat_memory=ChatMessageHistory()):
    model = get_model("ChatGPT", openai_api_key=openai_api_key)
    system_prompt = """
Bạn là một trợ lí ảo nhằm trả lời các CÂU HỎI cho khách hàng của VNGCloud.
Câu trả lời của bạn phải có liên quan đến NGỮ CẢNH được cung cấp. Nếu không liên quan hãy yêu cầu cung cấp thêm thông tin.
Bạn PHẢI trả lời bằng TIẾNG VIỆT

NGỮ CẢNH:
{context}

CÂU HỎI:
"""

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{question}"),
        ]
    )

    rag_chain = make_rag_chain(model, retriever, rag_prompt=prompt)
    chain = create_memory_chain(model, rag_chain, chat_memory)
    return chain


def ask_question(chain, query):
    response = chain.invoke(
        {"question": query},
        config={"configurable": {"session_id": "foo"}}
    )
    return response