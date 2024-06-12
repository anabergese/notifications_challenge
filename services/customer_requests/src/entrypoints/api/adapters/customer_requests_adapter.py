from fastapi import HTTPException
from services.notifications.src.entrypoints.api.ports.notifier_port import NotifierPort
class CustomerRequestsAdapter:
    def __init__(self, slack_notifier: NotifierPort, email_notifier: NotifierPort):
        self.slack_notifier = slack_notifier
        self.email_notifier = email_notifier

    def process_request(self, topic: str, description: str):
        if self.slack_notifier.validate_topic(topic):
            self.slack_notifier.notify(description)
        elif self.email_notifier.validate_topic(topic):
            self.email_notifier.notify(description)
        else:
            raise HTTPException(status_code=400, detail="Unknown topic. Try again.")
