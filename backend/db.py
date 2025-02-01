from datetime import datetime, timezone
from pymongo import MongoClient

client = MongoClient(MONGO_URI)

database = client["readcap"]
collection = database["messages"]


def send_message_DB(message, user):
    new_message = {"name": user, "message_content": message, "message_type": "text", "time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    insert_result = collection.insert_one(new_message)
    print("Inserted document ID:", insert_result.inserted_id)
    return

def get_messages():
    messages = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
    return messages


send_message_DB("hi", "mayank")