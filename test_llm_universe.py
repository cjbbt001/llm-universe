import os
from dotenv import load_dotenv

# Must specify path explicitly when running from stdin/pipe
load_dotenv(os.path.expanduser("~/llm-universe/.env"))

from zhipuai import ZhipuAI

key = os.getenv("ZHIPUAI_API_KEY")
print(f"Key loaded: {bool(key)}")
client = ZhipuAI()
models = client.models.list()
print(f"智谱 OK，{len(models.data)} 个模型")
