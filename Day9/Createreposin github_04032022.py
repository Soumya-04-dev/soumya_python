import requests
import json

# Github Token: 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
url = "https://api.github.com/user/repos"
token = "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"
headers = {"Authorization": f'token {token}'}
# repository_name = input("Enter the name of the repository ")
# data = {"name": f"{repository_name}"}
# username = input("Enter your username ")
# url_delete = f"https://api.github.com/repos/{username}/{repository_name}"
# r = requests.get("https://api.github.com/users/Soumya-04-dev")
'''
# requests.delete(url_delete, headers=headers)
for user_create_repo in range(2):
    repository_name = input("Enter the name of the repository ")
    data = {"name": f"{repository_name}"}
    requests.post(url, data=json.dumps(data), headers=headers)
'''
r = requests.get(url, headers=headers)
print(r)
