import os
from typing import List, Iterable, Any
import re

from dotenv import load_dotenv
from langchain.memory import ChatMessageHistory
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.retrievers import BaseRetriever
from langchain_core.runnables.history import RunnableWithMessageHistory

from basic_chain import get_model
from rag_chain import make_rag_chain

def remove_thinking(response):
    response.content = re.sub(r".*</think>\s*", "", response.content, flags=re.DOTALL)
    return response


def create_memory_chain(llm, base_chain, chat_memory):
    contextualize_q_system_prompt = """Cung cấp ĐOẠN HỘI THOẠI và CÂU HỎI, đánh giá CÂU HỎI có liên quan đến ĐOẠN HỘI THOẠI hay không. Nếu có vui lòng diễn giải lại, ngược lại GIỮ NGUYÊN CÂU HỎI."""

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )

    runnable = contextualize_q_prompt | llm | remove_thinking | base_chain

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        return chat_memory

    with_message_history = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        input_messages_key="question",
        history_messages_key="chat_history",
    )

    return with_message_history


class SimpleTextRetriever(BaseRetriever):
    docs: List[Document]
    """Documents."""

    @classmethod
    def from_texts(
            cls,
            texts: Iterable[str],
            **kwargs: Any,
    ):
        docs = [Document(page_content=t) for t in texts]
        return cls(docs=docs, **kwargs)

    def _get_relevant_documents(
            self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        return self.docs