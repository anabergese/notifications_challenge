import json

def process_message(message):
    print(f"Processing message from worker: {message}")
    message_data = json.loads(message)
    print(f"Message ID: {message_data['id']}")
    print(f"Topic: {message_data['topic']}")
    print(f"Description: {message_data['description']}")
