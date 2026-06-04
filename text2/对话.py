from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import os
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model='deepseek-ai/DeepSeek-V4-Flash',  #模型的具体版本
    model_provider='openai',
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL')
)

# 多轮对话
# coversation = [
#     SystemMessage(content="你是一个有帮助的AI助手"),
#     HumanMessage(content="你好，我叫GGB"),
#     AIMessage(content="你好！GGB,有什么我可以帮助你的吗？ "),
#     HumanMessage(content="我叫什么名字？")
# ]
# response = llm.invoke(coversation).content
# print(response)

# # 从配置读取对话模板
# prompt_template = [
#     {"role":"system","content":"你是一个{role}"},
#     {"role":"user","content":"请解释{topic}"}
# ]
#
# # 动态填充
# message = [
#     {
#         "role":t["role"],"content":t["content"].
#     format(role="翻译官",topic="机器翻译")
#     } for t in prompt_template
# ]
# response = llm.invoke(message).content
# print(response)



