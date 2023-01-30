import requests
import json

url = "https://github.com/jkweil125/github_action/blob/main/.github/workflows/learn-github-actions.yml/dispatches"

data = {
    'owner': 'jkweil125',
    'repo': 'github_action',
    'workflow_id': 'learn-github-actions.yaml',
    'ref': 'main',
}

headers = {
    'auth': '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'
}

response = requests.post(url,headers=headers,data=data)

print(response)