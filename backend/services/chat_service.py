from openai import OpenAI
from backend.core.config import(
 DEEPSEEK_API_KEY,
BASE_URL,
)
client=OpenAI(
     api_key=DEEPSEEK_API_KEY,
     base_url=BASE_URL
    )
def chat(message):
    response=client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role":"user",
                "content":message,
            }
        ]
    )
    return response.choices[0].message.content