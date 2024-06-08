from src.infrastructure.repositories.customer_request_repository import CustomerRequestRepository
# from src.infrastructure.notifications.notification_service import NotificationService
from src.domain.models.customer_request import CustomerRequest

class CustomerRequestService:
    def __init__(self):
        self.repository = CustomerRequestRepository()
        # self.notification_service = NotificationService()

    def process_request(self, topic: str, description: str):
        request = CustomerRequest(topic=topic, description=description)
        self.repository.save(request)
        self.notification_service.send_notification(request)
