"""
import os
import dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import StrOutputParser
dotenv.load_dotenv()

llm= init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',  #模型的具体版本
    model_provider='openai',    #模型的供应商
    api_key=os.getenv('GJ_API_KEY'),  #key
    base_url=os.getenv('GJ_BASE_URL')
)

parser = StrOutputParser()

prompt = PromptTemplate.from_template(
    "介绍一下{name}，他今年{age}岁"
)

chain=prompt|llm|parser
res = chain.invoke({"name":"小吴","age":10})
print(res)


"""


