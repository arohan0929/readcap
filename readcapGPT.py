import json
import openai


def summarize_chat(messages):
    """
    Summarizes a list of chat messages using OpenAI's API.

    :param messages: List of chat messages to be summarized.
    :return: A summary of the chat messages.
    """
    # Join messages into a single string
    chat_content = "\n".join(messages)

    # Call OpenAI's API to summarize the chat
    response = openai.Completion.create(
        engine=deployment_name,
        prompt=f"Summarize the following chat:\n{chat_content}",
        max_tokens=150,
        temperature=0.5
    )

    # Extract the summary from the response
    summary = response.choices[0].text.strip()
    return summary

# Example usage
messages = [
    "Hey, how are you?",
    "I'm good, thanks! How about you?",
    "Doing well, just working on a project.",
    "That's great! What project are you working on?"
]

summary = summarize_chat(messages)
print("Chat Summary:", summary)

