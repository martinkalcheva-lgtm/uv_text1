from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="glm-4-flash",       # 智谱模型名，免费
    api_key=os.getenv("ZP_API_KEY"),
    base_url=os.getenv("ZP_BASE_URL")
)

print(llm.invoke("你好").content)