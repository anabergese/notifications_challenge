
import redis

def main():
    r = redis.StrictRedis(host="localhost", port=6379)
    pubsub = r.pubsub()
    pubsub.subscribe('db_service')

    print("Subscribed to 'db_service'. Waiting for messages...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received message: {message['data']}")

if __name__ == "__main__":
    main()