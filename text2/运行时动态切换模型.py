from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model_provider="openai",
    base_url=os.getenv("GJ_BASE_URL"),
    api_key=os.getenv("GJ_API_KEY"),
    temperature=0
)

result1 = llm.invoke(
    "你好",
    config={"configurable":{"model":"deepseek-ai/DeepSeek-V4-Flash"}}
)

result2 = llm.invoke(
    "你好",
    config={"configurable":{"model":"Pro/moonshotai/Kimi-K2.6"}}
)

print(result1.content)
print(result2.content)
