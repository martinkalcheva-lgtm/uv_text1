from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.callbacks import get_usage_metadata_callback

load_dotenv()

llm = init_chat_model(
    model='deepseek-ai/DeepSeek-V4-Flash',
    model_provider='openai',
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL')
)

question =[
        "你好",
        "苹果创作者名字(只要名字)",
        "苹果是在地上种出来的还是树上？两者选其一回答"
    ]
with get_usage_metadata_callback() as cb:
    result = llm.batch(question)

    for q,r in zip(question,result):
        print(f"q:{q}")
        print(f"r:{r.content}")

print("\n====Token统计====")
print(cb.usage_metadata)
