## Notification System Architecture
The product department requires a system to notify them when a customer requests assistance from a bot. The bot will send an HTTP request containing the topic (either "sales" or "pricing") and a description of the problem. The system needs to expose an API endpoint to receive this request and forward it to the appropriate channel (Slack or Email). The architecture must support future expansion to include more topics and channels.

## 
## Proposal
A distributed system with an Event-Driven Architecture (EDA) using FastAPI, Docker Compose, and Redis as the Message Broker. This would be put into production with Kubernetes. Justification for Choices Made:

- **FastAPI**: Expertise with the technology, it is fast and simple.
- **EDA**: It is a complete solution for the problem, designed to manage events.
- **EDA, Docker Compose, Redis & Kubernetes**: Scalable, well-known patterns.
- **Redis PubSub**: messaging technology that facilitates communication between different components in a **distributed system**. It is an **asynchronous** and scalable messaging service that separates the services responsible for producing messages from those responsible for processing them. This is beneficial as we can easily create more channels for additional topics that may be added in the future and it will also be easy to add more services that subscribe to a certain channel if necessary (for example if we need to add a new database service).

### The Docker-Compose Containers structure is:
- redis
- workers
- tests

### Pipeline of Events
1. A notification is received from CustomerBot. 
2. FastAPI entry point: POST /notify creates NotificationCreated event and share it with Messagebus.
3. The Messagebus handle the event: publish it in the "db_service" channel in Redis (PubSub),and saves it in a Redis database.
3. The Worker db_handler subscribed to that channel receives the event and sends it to the "notifications_services" channel in Redis.
5. The NotificationOrchestrator subscribes to that channel, make a request to the Redis database to retrieve that notification.
6. The NotificationOrchestrator associates the notification to its corresponding notifier, based on the topic (pricing or sales).
7. EmailNotifier (pricing topic) and SlackNotifier (sales topic) implement the logic of sending the notification to the corresponding channel (sales-->slack, pricing -->email).

See more here: https://app.eraser.io/workspace/71vqPEdk9ueJvUE0mJ0r


How to run the app

Go to the main folder of the project.
Run: 'docker compose up'.



Trello Dashboard

https://trello.com/b/PfWLSu5I/notification-system
