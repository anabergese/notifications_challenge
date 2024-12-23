Notification System Architecture

The product department requires a system to notify them when a customer requests assistance from a bot. The bot will send an HTTP request containing the topic (either "sales" or "pricing") and a description of the problem. The system needs to expose an API endpoint to receive this request and forward it to the appropriate channel (Slack or Email). The architecture must support future expansion to include more topics and channels.

See more here: https://app.eraser.io/workspace/71vqPEdk9ueJvUE0mJ0r


How to run the app

Go to the main folder of the project.
Run: 'docker compose up'.



Trello Dashboard

https://trello.com/b/PfWLSu5I/notification-system

```
notifications
├─ .dockerignore
├─ Dockerfile
├─ Docs
├─ README.md
├─ compose.yaml
├─ mypy.ini
├─ requirements.txt
├─ src
│  ├─ __init__.py
│  ├─ application
│  │  ├─ __init__.py
│  │  ├─ db_main.py
│  │  ├─ db_service.py
│  │  ├─ notifier.py
│  │  ├─ notifier_main.py
│  │  └─ notifiers.py
│  ├─ config.py
│  ├─ domain
│  │  ├─ __init__.py
│  │  ├─ enums.py
│  │  ├─ events.py
│  │  └─ models.py
│  ├─ entrypoints
│  │  ├─ __init__.py
│  │  ├─ bootstrap.py
│  │  ├─ dependencies.py
│  │  ├─ exception_handlers
│  │  │  ├─ __init__.py
│  │  │  └─ handlers.py
│  │  ├─ main.py
│  │  └─ routes
│  │     ├─ __init__.py
│  │     ├─ models.py
│  │     └─ routes.py
│  ├─ infrastructure
│  │  ├─ __init__.py
│  │  └─ repositories
│  │     └─ __init__.py
│  ├─ seedwork
│  │  ├─ __init__.py
│  │  ├─ application
│  │  │  ├─ __init__.py
│  │  │  ├─ redis_consumer.py
│  │  │  └─ redis_publisher.py
│  │  ├─ domain
│  │  │  └─ __init__.py
│  │  └─ intrastructure
│  │     └─ __init__.py
│  └─ service_layer
│     ├─ __init__.py
│     ├─ handlers.py
│     └─ messagebus.py
└─ tests
```