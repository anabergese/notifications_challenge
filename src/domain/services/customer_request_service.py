from src.domain.models.customer_request import CustomerRequest

class CustomerRequestService:
    def process_request(self, topic: str, description: str):
        # Create a customer request object
        request = CustomerRequest(topic=topic, description=description)
        # Save request to the repository
        # self.repository.save(request)
        # Send notification
        # self.notification_service.send_notification(request)
