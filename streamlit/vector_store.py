import logging
import os
from typing import List

from langchain_openai import OpenAIEmbeddings
from modules import utils
from langchain_community.vectorstores import Chroma
from local_loader import get_document_text
from remote_loader import download_file
from splitter import split_documents
from dotenv import load_dotenv
from langchain_core.vectorstores import VectorStore
from langchain_core.embeddings import Embeddings
from langchain_postgres.vectorstores import PGVector
from time import sleep

EMBED_DELAY = 0.02  # 20 milliseconds

ENV_FILE_PATH = "/Users/cuongdm8499/Me/git-cuongpiger/secret/work/vngcloud/ai-platform/env"
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
MAX_TOKENS = 32700
COLLECTION_NAME = "my_docs"
envs = utils.load_env_to_dict(ENV_FILE_PATH)


# This is to get the Streamlit app to use less CPU while embedding documents into Chromadb.
class EmbeddingProxy:
    def __init__(self, embedding):
        self.embedding = embedding

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        sleep(EMBED_DELAY)
        return self.embedding.embed_documents(texts)

    def embed_query(self, text: str) -> List[float]:
        sleep(EMBED_DELAY)
        return self.embedding.embed_query(text)


# This happens all at once, not ideal for large datasets.
def create_vector_db(embeddings: Embeddings) -> VectorStore:
    # Create a vectorstore from documents
    # this will be a chroma collection with a default name.
    db: PGVector = PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=envs["POSTGRESQL_URI_2"],
        use_jsonb=True,
    )

    return db


def find_similar(vs, query):
    docs = vs.similarity_search(query)
    return docs