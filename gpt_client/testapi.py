from openai import OpenAI

client = OpenAI(
    api_key="sk-BY7ssQq2B9Vhv8JDrqIWHZSETyV2ZFX5ppfy8eHDhQehWqvf",
    base_url="https://ai.nengyongai.cn/v1"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "1+1=多少"}],
    stream=True
)

for chunk in response:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
