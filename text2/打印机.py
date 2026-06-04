from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import time
import asyncio

load_dotenv()

llm = init_chat_model(
    model="glm-4-flash",       # 智谱模型名，免费
    model_provider='openai',    #模型的供应商
    api_key=os.getenv("ZP_API_KEY"),
    base_url=os.getenv("ZP_BASE_URL")
)

# print("AI回答：")
# full_message = None
# for t in llm.stream("你好"):
#     full_message = t if full_message is None else full_message + t
#     print(t.content,end='',flush=True)
#     time.sleep(0.2)


# 监听
# async def stream_events():
#     async for event in llm.astream_events("你好"):
#         if event["event"] == "on_chat_model_start":
#             print("开始")
#         elif event["event"]=="on_chat_model_stream":
#             print("-", end="", flush=True)
#         elif event["event"]=="on_chat_model_end":
#             print("\n结束")
# asyncio.run(stream_events())



# async def batch_example():
#     questions = [
#         "你好",
#         "苹果创作者名字",
#         "苹果是在地上种出来的还是树上？两者选其一回答"
#     ]
#     # 同步batch()
#     # responses = llm.batch(questions)
# #     for q,r in zip(questions,responses):
# #         print(f'Q:{q}')
# #         print(f'R:{r.content}\n')
# #     异步abatch
#     responses = await llm.abatch(questions)
#     for q,r in zip(questions,responses):
#         print(f'Q:{q} \n R:{r.content}\n')
# asyncio.run(batch_example())

