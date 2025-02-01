from datetime import datetime, timezone
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://mayankgoel214:qXtFErtjLRcsK18Q@readcap.rwhg1.mongodb.net/?retryWrites=true&w=majority&appName=Readcap"

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


print (get_messages())