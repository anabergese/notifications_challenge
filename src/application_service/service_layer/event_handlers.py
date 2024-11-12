from domain.events import NotificationFailed
from domain.system_events import Event


def send_service_status_notification(event: Event):
    print(f"Event {event} sent to external system for monitoring")


def send_notification_failed_to_slack(event: NotificationFailed):
    print(f"Slack Notification: A notification failed due to: {event.reason}")
