import requests
import json

url = "https://github.com/repos/jkweil125/github_action/actions/workflows/learn-github-actions.yaml"

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