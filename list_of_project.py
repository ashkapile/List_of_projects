import requests
from requests.auth import HTTPBasicAuth
import json
#import os

email = "ashvinikapile123@gmail.com"

url = "https://ashvinikapile123.atlassian.net/rest/agile/1.0/board/1/issue"

API_TOKEN = "JIRA_API_TOKEN"

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