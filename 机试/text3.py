import dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.callbacks import get_usage_metadata_callback

dotenv.load_dotenv()

llm = init_chat_model(
    model='deepseek-ai/DeepSeek-V4-Flash',
    model_provider='openai',
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL')
)

count = [
    SystemMessage(content="你是一个湖南旅游导游"),
    HumanMessage(content="你好我叫小果"),
    AIMessage(content="你好我是你的导游有什么需要帮助的吗？"),
    HumanMessage(content="我叫什么？")
]

with get_usage_metadata_callback() as a:
    result = llm.invoke(count)
    print(result.content)

print("\n====Token统计====")
print(result.usage_metadata)
print(result.usage_metadata['total_tokens'])