import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace

from dotenv import load_dotenv

from modules import utils

MISTRAL_ID = "mistralai/Mistral-7B-Instruct-v0.1"
ZEPHYR_ID = "HuggingFaceH4/zephyr-7b-beta"

ENV_FILE_PATH = "/Users/cuongdm8499/Me/git-cuongpiger/secret/work/vngcloud/ai-platform/env"
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
MAX_TOKENS = 32700
COLLECTION_NAME = "my_docs"

envs = utils.load_env_to_dict(ENV_FILE_PATH)


def get_model(repo_id=ZEPHYR_ID, **kwargs):
    chat_model = ChatOpenAI(
        openai_api_key="EMPTY",
        openai_api_base=envs['VLLM_HOST_URL_2'] + "/v1/",
        model_name=MODEL_NAME,
        max_tokens=MAX_TOKENS,
        streaming=True,
        temperature=0,
    )

    return chat_model


def basic_chain(model=None, prompt=None):
    if not model:
        model = get_model()
    if not prompt:
        prompt = ChatPromptTemplate.from_template("Tell me the most noteworthy books by the author {author}")

    chain = prompt | model
    return chain


def main():
    load_dotenv()

    prompt = ChatPromptTemplate.from_template("Tell me the most noteworthy books by the author {author}")
    chain = basic_chain(prompt=prompt) | StrOutputParser()

    results = chain.invoke({"author": "William Faulkner"})
    print(results)


if __name__ == '__main__':
    main()
