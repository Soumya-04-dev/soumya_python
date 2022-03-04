import requests
import json

# Github Token: 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

'''
for user_create_repo in range(2):
    repository_name = input("Enter the name of the repository ")
    data = {"name": f"{repository_name}"}
    requests.post(url, data=json.dumps(data), headers=headers)
'''
url = "https://api.github.com/users/Soumya-04-dev/repos"
token = "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"
headers = {"Authorization": f'token {token}'}
response = requests.get(url, headers=headers)
print(type(response.text))
# str -> dict --json.loads()
data = json.loads(response.text)
for i in data:
    print(i["name"])
