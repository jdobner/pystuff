#! /usr/bin/env python3

from together import Together

client = Together() # auth defaults to os.environ.get("TOGETHER_API_KEY")

response = client.chat.completions.create(
    model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
    messages=[
      {
        "role": "user",
        "content": "is Iran safe now?"
      }
    ]
)
print(response.choices[0].message.content)