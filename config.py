import os
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

default_model_temperature = int(os.getenv("DEFAULT_MODEL_TEMPERATURE", "0"))
default_model_provider = os.getenv("DEFAULT_MODEL_PROVIDER", "OLLAMA").upper()
default_model_name = os.getenv("DEFAULT_MODEL_NAME", "gpt-4o")

ollama_hostname = os.getenv("OLLAMA_HOSTNAME","localhost")
ollama_port = os.getenv("OLLAMA_PORT","11434")

match default_model_provider:
    case "OPENAI":
        default_langchain_model = ChatOpenAI(model_name=default_model_name, temperature=default_model_temperature)
    case "ANTHROPIC":
        default_langchain_model = ChatAnthropic(model_name=default_model_name, temperature=default_model_temperature)
    case "OLLAMA":
        default_langchain_model = ChatOpenAI(
            model_name=default_model_name,
            temperature=default_model_temperature,
            openai_api_key="ollama",  # This can be any non-empty string
            openai_api_base=f"http://{ollama_hostname}:{ollama_port}/v1",
        )
    case _:
        raise ValueError(f"Unsupported model provider: {default_model_provider}")
