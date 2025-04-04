import os

from dotenv import load_dotenv
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate

from basic_chain import get_model
from filter import ensemble_retriever_from_docs
from memory import create_memory_chain
from rag_chain import make_rag_chain


def create_full_chain(retriever, chat_memory=ChatMessageHistory()):
    model = get_model("ChatGPT")
    system_prompt = """
Bạn tên là Orin, một ChatBot của VNGCloud AI Assistant, là một trợ lí ảo nhằm trả lời các CÂU HỎI cho khách hàng của VNGCloud.
Câu trả lời của bạn phải có liên quan đến NGỮ CẢNH được cung cấp. Nếu không liên quan hãy yêu cầu cung cấp thêm thông tin.
Bạn PHẢI trả lời bằng TIẾNG VIỆT.
Câu trả lời nên kèm theo hình ảnh minh hoạ nếu có thể.
Toàn bộ URL hình ảnh phải hiển thị định dạng sau: ![Mô tả](URL)

NGỮ CẢNH:
{context}

CÂU HỎI:
"""

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            # ("system", "Entire image URLs MUST display the following format: ![Description](IMAGE_URL)"),
            ("human", "{question}"),
        ]
    )

    rag_chain = make_rag_chain(model, retriever, rag_prompt=prompt)
    # chain = create_memory_chain(model, rag_chain, chat_memory)
    return rag_chain


def ask_question(chain, query):
    response = chain.stream(
        {"question": query},
        config={"configurable": {"session_id": "foo"}}
    )
    yield response