from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
import asyncio


load_dotenv()

llm = init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',  #模型的具体版本
    model_provider='openai',    #模型的供应商
    api_key=os.getenv('GJ_API_KEY'),  #key
    base_url=os.getenv('GJ_BASE_URL')
)

# 异步非流式写歌
async def img_chat():
    # 统计消耗Token

    result=await llm.ainvoke("写一首歌")
    print(result.content)

    print("\n====Token统计====")
    print(result.usage_metadata)
    print(result.usage_metadata['total_tokens'])


asyncio.run(img_chat())
