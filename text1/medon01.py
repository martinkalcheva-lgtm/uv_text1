from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# 加载.env文件
load_dotenv()

#硅胶
llm_claude = init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',  #模型的具体版本
    model_provider='openai',    #模型的供应商
    api_key=os.getenv('GJ_API_KEY'),  #key
    base_url=os.getenv('GJ_BASE_URL')
)

#智普
# llm_zp= init_chat_model(
#     model = 'glm-4-flash',  #模型的具体版本
#     model_provider='openai',    #模型的供应商
#     api_key=os.getenv('ZP_API_KEY'),  #key
#     base_url=os.getenv('ZP_BASE_URL')
# )
# print(llm_zp.invoke('用一句话介绍自己').content)


# print(llm_claude.invoke('用一句话介绍自己').content,end='\n')

conversation = [
    SystemMessage(content="你是一个有帮助的AI助手")
]




