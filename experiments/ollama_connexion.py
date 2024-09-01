import os
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama

default_model_temperature = float(os.getenv("DEFAULT_MODEL_TEMPERATURE", "0"))
default_model_provider = os.getenv("DEFAULT_MODEL_PROVIDER", "OLLAMA-NATIVE").upper()
default_model_name = os.getenv("DEFAULT_MODEL_NAME", "llama3.1")

ollama_hostname = os.getenv("OLLAMA_HOSTNAME","localhost")
ollama_port = os.getenv("OLLAMA_PORT","11434")

match default_model_provider:
    case "OLLAMA-NATIVE":
        default_langchain_model = ChatOllama(
            model=default_model_name,
            temperature=default_model_temperature,
            base_url=f"http://{ollama_hostname}:{ollama_port}",
        )
    case "OLLAMA-OPENAI":
        default_langchain_model = ChatOpenAI(
            model_name=default_model_name,
            temperature=default_model_temperature,
            openai_api_key="ollama",  # This can be any non-empty string
            openai_api_base=f"http://{ollama_hostname}:{ollama_port}/v1",
        )
    case _:
        raise ValueError(f"Unsupported model provider: {default_model_provider}")

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
print(f"config test:{default_model_provider}:{default_langchain_model.invoke(messages)}")