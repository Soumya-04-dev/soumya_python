'''emp_info = {'id': 1, 'name': 'Soumya', 'class': 5}# to find keys in dictionary
emp_info1 = input()
if  emp_info1 in emp_info:
    print("Key is available")
   '''
'''___________________________________________________________
# to find the square of numbers print in Dictionary
user_input = int(input())
dict = {}
for i in range(1,user_input):
    dict[i] = i ** 2  # i * i
print(dict)
___________________________________________________________________'''
'''
list1 = [1, 2, 3, 4]
Str1 = 'Work'
# output: ['Work1', 'Work2', 'Work3', 'Work4']
list2 = []
for i in list1:
    list2.append(Str1 + str(i))
print(list2)
'''
'''
list1 = [{}, {1,2}, {}, {}, {}, {}]
# to check dictionary is empty or not
is_empty = True
for dic in list1:
    if dic:
        is_empty = False
        break
if is_empty == True :
    print("dictionary is empty")
else:
    print("dictionary is not empty")'''
# --------------------------------------------------------------------------

dic1 = {'1': ['a', 'b'], '2': ['c', 'd']}
''' output: 
ac
ad
bc
bd
'''
dic2 = {}
# for i in dic1:
# dic2= dic1.values()
list1 = list(dic1.values())
print(list1)

list2 = []
for j in list1[0]:
    for m in list1[1]:
        #  list2.append(j+m)
        print(j + m)
# print(list2)
