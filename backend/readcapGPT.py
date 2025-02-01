import os  
import base64
from openai import AzureOpenAI  
import openai
import json

client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",
)

def ai_respond(messages):
    completion = client.chat.completions.create(  
        model=deployment,
        messages=messages,
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,
        stop=None,  
        stream=False
    )
    print(completion.to_json())  
with open('messages.json', 'r') as file:
        messages_data = json.load(file)

texts = "\n".join(
        f"{msg['name']} ({msg['time']}): {msg['message_content']}" for msg in messages_data
    )
def summarize_chat():
    user_input = input()
    chat_prompt = [
        {
            "role": "system",
            "content": "You are the best assistant that summarizes and analyzes chat messages in a group chat."
        },
        {
            "role": "user",
            "content": f"{user_input}: {texts}"
        },
    ] 

    messages = chat_prompt
    ai_respond(messages)
    
summarize_chat()