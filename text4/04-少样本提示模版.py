from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate

# 准备示例数据
ep = [
    {"input": "高兴", "output": "开心"},
    {"input": "难过", "output": "悲伤"},
    {"input": "生气", "output": "愤怒"}
]

# 定义格式化模版
e_f = PromptTemplate(
    template="输入: {input}\n输出: {output}",
    input_variables=["input", "output"]
)

# 创建少样本提示模板
few_shot_prompt = FewShotPromptTemplate(
    examples=ep,
    example_prompt=e_f,
    prefix="以下是一些同义词转换的例子：",    # 示例前的说明文字
# 关键修复：{{output}} 转义，不作为变量
    suffix="\n输入: {input}\n输出:",         # 示例后的实际问题
    input_variables=["input"]
)

print(few_shot_prompt.invoke({"input": "兴奋"}))