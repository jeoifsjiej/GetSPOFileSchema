# scripts/pnp_sync.py
"""
Simple sample to list files/folders in a SharePoint library using Microsoft Graph REST endpoints.
This script uses client credential flow or interactive auth externally. Do NOT embed secrets.
All values here are fictional placeholders.
"""
import json
import requests

# === プレースホルダ（実データを入れないこと） ===
TENANT = "example.onmicrosoft.com"
SITE_ID = "sites/example-site-id"   # placeholder
DRIVE_ID = "b!driveIdExample"       # placeholder
ACCESS_TOKEN = "<ACCESS_TOKEN_PLACEHOLDER>"

def get_drive_children(site_id, drive_id, token):
    url = f"https://graph.microsoft.com/v1.0/{site_id}/drives/{drive_id}/root/children"
    headers = {"Authorization": f"Bearer {token}"}
    items = []
    next_url = url
    while next_url:
        r = requests.get(next_url, headers=headers)
        r.raise_for_status()
        data = r.json()
        items.extend(data.get("value", []))
        next_url = data.get("@odata.nextLink")
    return items

def to_structure(items):
    out = []
    for it in items:
        out.append({
            "id": it.get("id"),
            "name": it.get("name"),
            "webUrl": it.get("webUrl"),
            "isFolder": "folder" in it,
            "size": it.get("size", 0)
        })
    return out

def main():
    if ACCESS_TOKEN.startswith("<"):
        print("ACCESS_TOKEN is placeholder. Replace with a valid token in a secure way.")
        return
    items = get_drive_children(SITE_ID, DRIVE_ID, ACCESS_TOKEN)
    structure = to_structure(items)
    with open("../samples/sample_structure.json", "w", encoding="utf-8") as f:
        json.dump(structure, f, ensure_ascii=False, indent=2)
    print("Exported sample_structure.json")

if __name__ == "__main__":
    main()
