from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage,HumanMessage

prompt=ChatPromptTemplate.from_messages([
    ("system","你是一个AI助手"),
    MessagesPlaceholder(variable_name="history"),# 对话历史插槽
#     等同于上面("placeholder","{history}")
    ("human","{input}")
])

# 调用时传入历史消息列表
messages = prompt.invoke({
    "history": [
        HumanMessage(content="什么是Python？"),
        AIMessage(content="Python是一种通用编程语言。"),
    ],
    "input": "它有什么特点？"
})
print(messages)