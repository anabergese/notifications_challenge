from enum import Enum

class TopicEnum(str, Enum):
    SALES = "sales"
    PRICING = "pricing"
    # Nuevos tópicos se pueden agregar aquí