import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

email = "ashvinikapile123@gmail.com"

url = "https://ashvinikapile123.atlassian.net/rest/agile/1.0/board/1/issue"

API_TOKEN = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth(email, API_TOKEN)

if not API_TOKEN:
    raise ValueError("Missing API Token in .env")

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