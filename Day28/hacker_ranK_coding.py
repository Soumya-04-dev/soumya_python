import re

'''from itertools import permutations
n, k = input().split()
l1 = []
for i in n:
    l1.append(i)
l1.sort()
print(l1)
list2 = list(permutations(l1, int(k)))
print(list2)

for j in list2:
    x = "".join(j)
    print(x)
'''

'''
#mobileno validation with Regex
n = int(input())
for i in range(n):
    phone_n0 = input()
    if re.match('^[789][0-9]{9}$', phone_n0):
        print(True)
    else:
        print(False)

import re

n = int(input())
for i in range(n):
    credit_no = input()
    if re.match(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', credit_no) and not re.search(r'([\d])\1-?\1\1',
                                                                                               credit_no):

        print("Valid")
    else:
        print("Invalid")
'''

# --1. Take a string e.g my_name =  my name is Sohil
# output:
# ym eman si lihos
# --2. One dic1= {'A': 65, 'B':66, 'C': 67, 'D': 68 }
# output: dic1 = {'65': A, '66':B, '67': C, '68': D '}

n = input()
