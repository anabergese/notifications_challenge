## Notification System Architecture
The product department requires a system to notify them when a customer requests assistance from a bot. The bot will send an HTTP request containing the topic (either "sales" or "pricing") and a description of the problem. The system needs to expose an API endpoint to receive this request and forward it to the appropriate channel (Slack or Email). The architecture must support future expansion to include more topics and channels.

## 
## Proposal
A distributed system with an Event-Driven Architecture (EDA) using FastAPI, Docker Compose, and Redis as the Message Broker. This would be put into production with Kubernetes. Justification for Choices Made:

- **FastAPI**: Expertise with the technology, it is fast and simple.
- **EDA**: It is a complete solution for the problem, designed to manage events.
- **EDA, Docker Compose, Redis & Kubernetes**: Scalable, well-known patterns.
- **Redis Streams & Consumer Groups**
- **Functional Programming**

### The Docker-Compose Containers structure is:
- redis
- api
- workers
- tests

### Pipeline of Events
1. A notification is received from CustomerBot. 
2. FastAPI entry point: POST /notify creates NotificationCreated event and shares it with Messagebus.
3. The Messagebus handles the event: publish it in the Redis Streams.
4. The NotificationOrchestrator subscribes to Redis Streams.
5. The NotificationOrchestrator associates the event is sent to its corresponding notifier, based on the topic (pricing or sales).
6. EmailNotifier (pricing topic) and SlackNotifier (sales topic) implement the logic of sending the notification to the corresponding channel (sales-->slack, pricing -->email).

### Trello Dashboard
https://trello.com/b/PfWLSu5I/notification-system

### Full Documentation
See more here: https://app.eraser.io/workspace/71vqPEdk9ueJvUE0mJ0r

##
## How to run the app

### Run only on dev mode
Go to the main folder of the project. Run: 
'docker compose up'.

### Run with tests
Go to the main folder of the project. Run:
'docker compose --profile testing up'


