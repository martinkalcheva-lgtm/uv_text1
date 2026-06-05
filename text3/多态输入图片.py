import base64
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatOpenAI(
    model="Qwen/Qwen3-VL-8B-Instruct",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL')
)


with open("./dog.jpg", "rb") as f:
    image_data=f.read()

message = HumanMessage(
    content=[
        {"type":"text","text":"这图上是什么动物？"},
        {"type":"image_url","image_url":{"url": f"data:image/jpeg;base64,{base64.b64encode(image_data).decode()}"}}
    ]
)

response=llm.invoke([message])
print(response.content)