import requests
import json

'''
jsonpayload_dict1 = {'url': 'https://api.github.com/user/repos',
                    'token': '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 '
                    }
headers = {"Authorization": f'token {jsonpayload_dict1["token"]}'}


def create_repo_github(url, headers, repo_name):
    for i in range(1):
        # repo_name = input("Enter repo name")
        data = {"name": f'repo_name {repo_name}'}
        response1 = requests.post(url, data=json.dumps(data), headers=headers)
        print(response1.status_code)

    jsonpayload_dict2 = {'url': 'https://api.github.com/users/Soumya-04-dev/repos',
                         'token': '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'
                         }
    response2 = requests.get(jsonpayload_dict2['url'], headers=headers)
    data1 = json.loads(response2.text)
#    print(response2.text)
    for dic in data1:
        if dic["name"] == 'repo_name-test3':
            return True

    return False

repo_name = input("Enter the name of repo")
store_var = create_repo_github(jsonpayload_dict1['url'], headers, repo_name)
print(store_var)
'''
