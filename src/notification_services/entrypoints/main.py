from config import create_redis_connection
from domain.notifiers import EmailNotifier, SlackNotifier
from worker import Worker


def main():
    redis_conn = create_redis_connection()

    notifiers = {
        "pricing": EmailNotifier(),
        "sales": SlackNotifier(),
    }

    worker = Worker(redis_conn, notifiers)
    worker.run()


if __name__ == "__main__":
    main()
