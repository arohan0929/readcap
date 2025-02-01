import json
import openai

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

texts = [
    "Hey, how are you?",
    "I'm good, thanks! How about you?",
    "Doing well, just working on a project.",
    "That's great! What project are you working on?"
]
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
