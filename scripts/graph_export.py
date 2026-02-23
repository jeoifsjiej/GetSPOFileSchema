# scripts/graph_export.py
"""
Sample using MSAL to get token and call Graph to list drive items.
This file uses placeholders and is for learning/demo only.
"""
import json
import msal
import requests

TENANT_ID = "your-tenant-id"  # placeholder
CLIENT_ID = "your-client-id"  # placeholder
CLIENT_SECRET = "<CLIENT_SECRET_PLACEHOLDER>"  # do NOT commit real secrets
SCOPE = ["https://graph.microsoft.com/.default"]
SITE_ID = "sites/example-site-id"
DRIVE_ID = "b!driveIdExample"

def acquire_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET
    )
    result = app.acquire_token_for_client(scopes=SCOPE)
    if "access_token" in result:
        return result["access_token"]
    raise Exception("Could not obtain access token")

def list_drive_items(token, site_id, drive_id):
    url = f"https://graph.microsoft.com/v1.0/{site_id}/drives/{drive_id}/root/children"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json().get("value", [])

def main():
    print("This script contains placeholders. Do not use real company data.")
    if CLIENT_SECRET.startswith("<"):
        print("CLIENT_SECRET is placeholder. Configure auth securely.")
        return
    token = acquire_token()
    items = list_drive_items(token, SITE_ID, DRIVE_ID)
    with open("../samples/graph-structure.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print("Saved graph-structure.json")

if __name__ == "__main__":
    main()
