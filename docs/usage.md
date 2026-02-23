# Usage

Required permissions
- Sites.Read.All or Files.Read.All for Graph API

Auth recommendations
- For development: MSAL device code or client credential (do not commit secrets)
- For quick tests: obtain token via Azure CLI and set ACCESS_TOKEN env var

Run examples
- python scripts/graph_export.py
- python scripts/pnp_sync.py

Security
- Do NOT include real tenant names, user accounts, or secrets in this repo.
