import openai

# Based on langchain_repo_openai_function_call.py
def call_openai_with_script(script: str):
    # Logic for calling the OpenAI API
    response = openai.Completion.create(engine="davinci", prompt=script)
    return response.choices[0].text.strip()
    
#### 

import os
import openai


with open('./code.py', 'r') as file:
    code_content = file.read()

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system',
         'content': 'You are a code review assistant. Provide detailed suggestions to improve the given Python code.'},
        {'role': 'user', 'content': code_content},
    ],
    temperature=0.5,
    max_tokens=1024
)

print(response)
print()
print(response.choices[0].message.content)