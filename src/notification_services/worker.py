import json
import redis

def redis_db():
    """
    Crea una conexión a la base de datos Redis y verifica que esté en funcionamiento.
    """
    try:
        db = redis.Redis(
            host="redis",
            port=6379,
            db=0,
            decode_responses=True,
        )
        
        # Verificar que Redis esté en funcionamiento
        db.ping()
        
        return db
    except redis.ConnectionError as con_err:
        print(f"Error al conectar con Redis: {con_err}")
        raise

def redis_queue_pop(db):
    """
    Extrae un elemento de la cola 'task_queue' en Redis de forma bloqueante.
    """
    try:
        print("Processing message from worker...")
        
        # `brpop` es una llamada bloqueante que espera hasta que un elemento esté disponible
        _, message_json = db.brpop("task_queue")
        
        # Decodificar el mensaje JSON
        message_data = json.loads(message_json)
        
        print(f"Message ID: {message_data['id']}")
        print(f"Topic: {message_data['topic']}")
        print(f"Description: {message_data['description']}")
        
        return message_json
    except (redis.ConnectionError, json.JSONDecodeError) as e:
        print(f"Error al procesar el mensaje: {e}")
        raise

if __name__ == "__main__":
    try:
        db = redis_db()
        
        # Aquí puedes poner un bucle infinito para procesar continuamente los mensajes de la cola
        while True:
            redis_queue_pop(db)
    except Exception as e_main:
        print(f"Error en el worker: {e_main}")


# import json

# def process_message(message):
#     print(f"Processing message from worker: {message}")
#     message_data = json.loads(message)
#     print(f"Message ID: {message_data['id']}")
#     print(f"Topic: {message_data['topic']}")
#     print(f"Description: {message_data['description']}")

