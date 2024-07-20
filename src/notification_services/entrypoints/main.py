from config import create_redis_connection
from worker import Worker
from domain.models import EmailNotifier, SlackNotifier

def main():
    redis_conn = create_redis_connection()

    notifiers = {
        'pricing': EmailNotifier(),
        'sales': SlackNotifier(),
        # Add more notifiers as needed
    }

    worker = Worker(redis_conn, notifiers)
    worker.run()

if __name__ == "__main__":
    main()
    