
```
notifications
├─ .dockerignore
├─ .pylintrc
├─ .venv
│  ├─ ...
├─ .vscode
│  └─ settings.json
├─ Dockerfile
├─ Docs
├─ README.md
├─ compose.yaml
├─ requirements.txt
└─ src
   ├─ application_service
   │  ├─ __init__.py
   │  ├─ domain
   │  │  ├─ __init_.py
   │  │  ├─ event_handlers.py
   │  │  └─ models.py
   │  ├─ entrypoints
   │  │  ├─ __init__.py
   │  │  ├─ main.py
   │  │  ├─ request_response_schema.py
   │  │  └─ routes
   │  │     └─ customer_requests_routes.py
   │  ├─ infrastructure
   │  │  └─ repositories
   │  │     └─ __init__.py
   │  └─ seedwork
   │     ├─ domain
   │     └─ infrastructure
   │        └─ __init__.py
   └─ notification_services
      ├─ __init__.py
      └─ entrypoints
         ├─ __init__.py
         ├─ domain
         │  ├─ __init__.py
         │  ├─ event_handlers.py
         │  └─ models.py
         ├─ main.py
         └─ routes
            ├─ __init__.py
            └─ notifications_routes.py

```