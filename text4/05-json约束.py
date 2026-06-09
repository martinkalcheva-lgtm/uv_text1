"""
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from pydantic import BaseModel,Field
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',  #模型的具体版本
    model_provider='openai',    #模型的供应商
    api_key=os.getenv('GJ_API_KEY'),  #key
    base_url=os.getenv('GJ_BASE_URL')
)

# 1. 定义目标JSON结构
class Prime(BaseModel):
    name:str = Field(description="名字")
    age:int = Field(description="年龄")

# 2. 构造解析器
json_p = JsonOutputParser(pydantic_object=Prime)

# 3. 将格式说明放入SystemMessage
res=llm.invoke([
    ("system",json_p.get_format_instructions()),
    ("user","小苏今年5岁")
])
c=res.content
print(type(c))  #<class 'str'>


# 4. 解析为Python字典
parsed_res = json_p.invoke(res)
print(type(parsed_res))  #data:<class 'dict'>

# 核心：解析字符串为Pydantic对象
data = json_p.parse(c)
print(f'data:{type(data)}') #data:<class 'dict'>

# 点语法取值
print(data['name'])
print(data['age'])
"""
import os
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain.chat_models import init_chat_model
from langchain.chat_models import init_chat_model
load_dotenv()

llm = init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',  #模型的具体版本
    model_provider='openai',    #模型的供应商
    api_key=os.getenv('GJ_API_KEY'),  #key
    base_url=os.getenv('GJ_BASE_URL')
)
# 2. 定义Pydantic模型
class CalendarEvent(BaseModel):
    name:str = Field(description="名字")
    date:str
    part:list[str]

# 3. 使用with_structured_output，返回一个新的Runnable
s_llm=llm.with_structured_output(schema=CalendarEvent)

# 4. 调用，直接返回Pydantic对象
result = s_llm.invoke("Alice and Bob are going to a science fair on Friday.")
print(result)