```
notifications
├─ .venv
├─ Dockerfile
├─ Docs
├─ README.md
├─ compose.yaml
├─ requirements.txt
└─ services
   ├─ customer_requests
   │  ├─ __init__.py
   │  └─ src
   │     ├─ __init__.py
   │     ├─ domain
   │     │  ├─ __init_.py
   │     │  └─ models
   │     │     ├─ __init_.py
   │     │     └─ customer_request.py
   │     ├─ entrypoints
   │     │  ├─ __init__.py
   │     │  └─ api
   │     │     ├─ __init__.py
   │     │     ├─ main.py
   │     │     └─ routes
   │     │        └─ customer_requests_routes.py
   │     ├─ infrastructure
   │     │  └─ repositories
   │     │     ├─ __init__.py
   │     │     └─ customer_request_repository.py
   │     └─ seedwork
   │        ├─ domain
   │        └─ infrastructure
   │           ├─ __init__.py
   │           └─ repositories.py
   └─ notifications
      └─ __init__.py

```