import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("JIRA_EMAIL")

url = os.getenv("JIRA_URL")

API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not email:
    raise ValueError("Missing email in .env")

if not url:
    raise ValueError("Missing url in .env")

if not API_TOKEN:
    raise ValueError("Missing API Token in .env")

auth = HTTPBasicAuth(email, API_TOKEN)

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))