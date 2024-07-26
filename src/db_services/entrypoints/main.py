from config import create_redis_connection
from db_service import DBService

def main():
    redis_conn = create_redis_connection()
    db_service = DBService(redis_conn)
    db_service.run()

if __name__ == "__main__":
    main()
    