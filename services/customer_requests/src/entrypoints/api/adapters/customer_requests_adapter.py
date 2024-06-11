from services.customer_requests.src.domain.models.customer_request import CustomerRequest

class CustomerRequestsAdapter:
    def process_request(self, topic: str, description: str):
        # Create a customer request object
        request = CustomerRequest(topic=topic, description=description)
        return request