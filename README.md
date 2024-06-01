```
notifications
├─ Docs
├─ README.md
├─ requirements.txt
└─ src
   ├─ Docker
   │  └─ Dockerfile.customer_request
   ├─ app
   │  ├─ __init__.py
   │  └─ main.py
   ├─ domain
   │  ├─ __init_.py
   │  ├─ models
   │  │  ├─ __init_.py
   │  │  └─ customer_request.py
   │  └─ services
   │     ├─ __init__.py
   │     └─ customer_request_service.py
   ├─ entrypoints
   │  ├─ __init__.py
   │  └─ fastapi
   │     ├─ __init__.py
   │     └─ routes
   │        └─ customer_request_route.py
   ├─ infrastructure
   └─ tests

```