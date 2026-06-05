import time
from langchain_openai import ChatOpenAI
from langchain_core.rate_limiters import InMemoryRateLimiter
import os
from dotenv import load_dotenv
load_dotenv()

a = InMemoryRateLimiter(
    requests_per_second=0.1,
    check_every_n_seconds=0.1
)
llm=ChatOpenAI(
    model="Qwen/Qwen3-VL-8B-Instruct",
    api_key=os.getenv('GJ_API_KEY'),
    base_url=os.getenv('GJ_BASE_URL')
)

def text_rate_limit(n=3):
    print("开始时间：", time.strftime("%X"))
    last = time.time()
    for i in range(n):
        t0 = time.time()
        resp = llm.invoke(f"第 {i} 次调用，简单回一句话就行")
        t1 = time.time()
        print(
            f"调用 {i} 完成，耗时 {t1 - t0:.2f}s，"
            f"距上次调用结束间隔 {t1 - last:.2f}s"
        )
        last = t1


text_rate_limit(3)