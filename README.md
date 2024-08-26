
│  └─ pyvenv.cfg
├─ .vscode
│  └─ settings.json
├─ Docs
├─ README.md
├─ compose.yaml
├─ src
│  ├─ application_service
│  │  ├─ __init__.py
│  │  ├─ domain
│  │  │  ├─ __init__.py
│  │  │  ├─ enums.py
│  │  │  └─ models.py
│  │  ├─ entrypoints
│  │  │  ├─ __init__.py
│  │  │  ├─ dependencies.py
│  │  │  ├─ lifespan.py
│  │  │  ├─ main.py
│  │  │  ├─ redis.py
│  │  │  └─ routes
│  │  │     ├─ __init__.py
│  │  │     ├─ models.py
│  │  │     └─ routes.py
│  │  ├─ infrastructure
│  │  │  └─ repositories
│  │  │     └─ __init__.py
│  │  ├─ requirements.txt
│  │  └─ service_layer
│  │     ├─ __init__.py
│  │     ├─ channels.py
│  │     ├─ redis_channel.py
│  │     └─ service.py
│  ├─ db_service
│  │  ├─ __init__.py
│  │  ├─ domain
│  │  │  ├─ __init__.py
│  │  │  ├─ enums.py
│  │  │  └─ models.py
│  │  ├─ entrypoints
│  │  │  ├─ __init__.py
│  │  │  ├─ config.py
│  │  │  ├─ db_service.py
│  │  │  └─ main.py
│  │  └─ requirements.txt
│  └─ notification_services
│     ├─ __init__.py
│     ├─ domain
│     │  ├─ __init__.py
│     │  ├─ enums.py
│     │  └─ notifiers.py
│     ├─ entrypoints
│     │  ├─ __init__.py
│     │  ├─ config.py
│     │  ├─ main.py
│     │  └─ notifier.py
│     └─ requirements.txt
└─ tests

```