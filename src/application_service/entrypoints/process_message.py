import json

def forward_event():
        # Código para reenviar el evento al canal adecuado
        print("Enviando slack slack slaaaaack!")

def process_message(message):
    print(f"Processing message from worker: {message}")
    message_data = json.loads(message)
    print(f"Message ID: {message_data['id']}")
    print(f"Topic: {message_data['topic']}")
    print(f"Description: {message_data['description']}")
    if message_data['topic'] == 'Pricing':
        print(f"Topic this for slack: {message_data['topic']}")
        forward_event()
        print("Enviado correctamente")
    else:
        # Requeue the job if it's not relevant for this worker
        print("Reenqueueing...")
