# l1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

'''
use of function:
reusable code and organize structure
readability increases
function will use when it calls
'''
'''
def find_length(name):
    b = len(name)
    print("The length of string is" + ' ' + str(b))

find_length('Soumya')

def changeme(list1):
    list1.append(2)
    print(list1)

changeme([1,2,3])'''
'''
No of Arguments:
1. required arguments :
'''
'''
def printme(name,city):
    print(name + " " + city)

#printme() #TypeError: printme() missing 1 required positional argument: 'name'
printme("sohil")  #TypeError: printme() missing 1 required positional argument: 'city'

'''
'''
#2. Keyword Arguments:

def printme(name,city):
    print(name + " " + city )
printme(name = "Soumya",city= "Pune",Age = 20) #TypeError: printme() got an unexpected keyword argument 'Age'

'''
'''
3. Default Arguments:

def printme(name,age = 35):
    print(name + " " + str(age) )
printme(name = "Soumya",age = 45)
printme(name = "Sohil")
'''

'''
4.variable length argument:

def info(arg1, *vartuple): # * stands for variable number of arguments. #** stands for variable keyword arguments
    print(arg1)
    print(vartuple)
    for item in vartuple:
        print(item)
info(10)
info(70, 60.5, 50)
def info1(arg1, **kwargs):
    for key in kwargs:
        print(arg1, key, kwargs[key])
info1(10)
info1(10,name = 'sohil', age = 28)
'''
'''
def info2(*args , **kwargs):
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
info2([10,20,20],name='sohil', age = 28, city = 'Pune')'''
'''
#To print a function which will reverse our name and print true and false

def palindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False

a = palindrome("sos")
print(a)
'''
# to create repo in github account
import requests
import json

jsonpayload_dict = {'url': 'https://api.github.com/user/repos',
                    'token': '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'
                    }

headers = {"Authorization": f'token {jsonpayload_dict["token"]}'}


def create_repo_github(url, headers, repo_name):
    for i in range(1):
        # repo_name = input("Enter repo name")
        data = {"name": f'repo_name {repo_name}'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        print(response.status_code)


repo_name = input("Enter the name of repo")
create_repo_github(jsonpayload_dict['url'], headers, repo_name)
