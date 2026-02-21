
import os
from ollama import Client

api_key = os.environ.get("OLLAMA_API_KEY")

if not api_key:
    raise ValueError("OLLAMA_API_KEY is not set!")

client = Client(
    host="https://ollama.com",
    headers={'Authorization': f'Bearer {api_key}'}
)

messages = [
    {"role": "user", "content": "Why is the sky blue?"}
]

for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
    print(part['message']['content'], end='', flush=True)


# import ollama
#
# response=ollama.generate(
#     model='deepseek-v3.2:cloud',
#     prompt='What is Machine learning?'
# )
# print(response['response'])

