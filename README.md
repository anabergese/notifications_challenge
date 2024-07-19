```
notifications
├─ Docs
├─ README.md
├─ compose.yaml
├─ src
│  ├─ application_service
│  │  ├─ __init__.py
│  │  ├─ domain
│  │  │  ├─ __init_.py
│  │  │  ├─ event_handlers.py
│  │  │  ├─ events.py
│  │  │  └─ models.py
│  │  ├─ entrypoints
│  │  │  ├─ __init__.py
│  │  │  ├─ main.py
│  │  │  ├─ models.py
│  │  │  └─ routes
│  │  │     └─ application_service_routes.py
│  │  ├─ infrastructure
│  │  │  └─ repositories
│  │  │     └─ __init__.py
│  │  ├─ requirements.txt
│  │  └─ seedwork
│  │     ├─ domain
│  │     └─ infrastructure
│  │        └─ __init__.py
│  └─ notification_services
│     ├─ __init__.py
│     ├─ domain
│     │  ├─ __init__.py
│     │  ├─ event_handlers.py
│     │  └─ models.py
│     ├─ entrypoints
│     │  ├─ __init__.py
│     │  ├─ main.py
│     │  └─ routes
│     │     ├─ __init__.py
│     │     └─ notifications_routes.py
│     ├─ requirements.txt
│     └─ worker.py
└─ tests

```