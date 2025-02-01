import os  
import base64
from openai import AzureOpenAI  
import openai
import json
from dotenv import load_dotenv

load_dotenv('readcap.env')

endpoint = os.getenv("ENDPOINT_URL")  
deployment = os.getenv("DEPLOYMENT_NAME")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")  

# Initialize Azure OpenAI Service client with key-based authentication    
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
            "content": "You are the best assistant that summarizes and analyzes chat messages in a group chat. Here are a few features I want you to implement"
                       "Event: Read the chats and search if an event place and time has been decided. Only do this if there is discussion of an event or meetup. If so put it in this format - {Event Location and time:(the location and time); people confirmed:(usernames of the people who have said yes);"
        },
        {
            "role": "user",
            "content": f"{user_input}: {texts}"
        },
    ] 

    messages = chat_prompt
    ai_respond(messages)
    
summarize_chat()


def start_ai(old_messages, message_prompt):
    return