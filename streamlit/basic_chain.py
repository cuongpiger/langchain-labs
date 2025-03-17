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
    if repo_id == "ChatGPT":
        chat_model = ChatOpenAI(
            openai_api_key="EMPTY",
            openai_api_base=envs['VLLM_HOST_URL_2'] + "/v1/",
            model_name=MODEL_NAME,
            max_tokens=MAX_TOKENS,
            streaming=True,
            temperature=0,
        )
    else:
        huggingfacehub_api_token = kwargs.get("HUGGINGFACEHUB_API_TOKEN", None)
        if not huggingfacehub_api_token:
            huggingfacehub_api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN", None)
        os.environ["HF_TOKEN"] = huggingfacehub_api_token

        llm = HuggingFaceHub(
            repo_id=repo_id,
            task="text-generation",
            model_kwargs={
                "max_new_tokens": 512,
                "top_k": 30,
                "temperature": 0.1,
                "repetition_penalty": 1.03,
                "huggingfacehub_api_token": huggingfacehub_api_token,
            })
        chat_model = ChatHuggingFace(llm=llm)
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
