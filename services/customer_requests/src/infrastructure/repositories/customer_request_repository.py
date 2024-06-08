from src.domain.models.customer_request import CustomerRequest
from src.seedwork.infrastructure.repositories import BaseRepository

class CustomerRequestRepository(BaseRepository):
    def __init__(self):
        self

    def save(self, customer_request: CustomerRequest):
        return customer_request

    def get_by_id(self):
        return self

    def list_all(self):
        return self

    def delete(self):
        return self

