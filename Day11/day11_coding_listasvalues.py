'''
To remove the values in keys
dict = {'c1': [10, 20, 30],'c2': [20, 30, 40],'c3': [12, 34]}
# {'c1' = [], 'c2' = [], 'c3' = []}
for key in dict:
    dict[key] = []
print(dict)
'''
'''
dict1 = {'V': 10,'VI':10,'VII':40,'VIII': 20,'IX':70,'X':80, 'XI':40,'XII':20 }
#To find out the frequency and print in dictionary
dict2 = {}
values= list(dict1.values())
print(values)
count = 0
for i in values:
    dict2[i] = values.count(i)
print(dict2)

'''
from collections import Counter

dict1 = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# To find out the frequency and print in dictionary
values = list(dict1.values())
print(Counter(values))
'''
emp_info = [{'id': 1, 'name': 'Soumya', 'class': 5}, {'id': 2, 'name': 'Sohil', 'class': 6},
            {'id': 3, 'name': 'Anjali', 'class': 7}]


# output: list of list: [[1,Soumya,5], [2,Sohil,6], [3,Anjali,7]]

output_list = []
test = []
for i in emp_info:
    test =  i.values()
    output_list.append(list(test))
print(output_list)

'''
