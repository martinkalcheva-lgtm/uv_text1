from langchain_core.prompts import PromptTemplate

# 方法一：调用partial方法固定部分变量
prompt = PromptTemplate.from_template(
"讲一个关于{topic}的{adjective}故事"
)
fixed_prompt=prompt.partial(adjective="有趣的")
print(fixed_prompt.invoke({"topic": "编程"}))

# 方法二
prompt2=PromptTemplate(
    template="讲一个关于{topic}的{adjective}故事",
    input_variables=["topic"],
    partial_variables={"style": "简单易懂"}
)
print(prompt.invoke({"concept": "递归"}))
