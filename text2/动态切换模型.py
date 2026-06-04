from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 加载.env文件
load_dotenv()

# 智普
llm_zp = init_chat_model(
    model="glm-4-flash",       # 智谱模型名，免费
    model_provider='openai',    #模型的供应商
    api_key=os.getenv("ZP_API_KEY"),
    base_url=os.getenv("ZP_BASE_URL")
)
#硅胶
llm_gj = init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',  #模型的具体版本
    model_provider='openai',    #模型的供应商
    api_key=os.getenv('GJ_API_KEY'),  #key
    base_url=os.getenv('GJ_BASE_URL')
)

#动态调用
for name,llm in [("智普",llm_zp),("硅胶",llm_gj)]:
    response=llm.invoke("用一句话介绍自己")
    print(f"{name}: {response.content}")