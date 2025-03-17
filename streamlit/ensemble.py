import os

from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.embeddings import Embeddings

from basic_chain import get_model
from rag_chain import make_rag_chain
from remote_loader import load_web_page
from splitter import split_documents
from vector_store import create_vector_db
from dotenv import load_dotenv


def ensemble_retriever_from_docs(embeddings: Embeddings) -> EnsembleRetriever:
    vs = create_vector_db(embeddings)
    vs_retriever = vs.as_retriever()

    ensemble_retriever = EnsembleRetriever(
        retrievers=[vs_retriever],
        weights=[1.0])

    return ensemble_retriever