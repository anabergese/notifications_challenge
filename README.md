```
notifications
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ HEAD
│  ├─ ORIG_HEAD
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  ├─ customer-requests
│  │     │  ├─ folders-organization
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           └─ main
│  ├─ objects
│  │  ├─ 00
│  │  │  ├─ 1fa733afde0b8d2dd69620ace282b74b51dc4a
│  │  │  ├─ 20402a8b839c30f09deccc2149bcf9cccda3f8
│  │  │  ├─ 239b70e7c745f6d1584c5117a6d186137d0351
│........
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