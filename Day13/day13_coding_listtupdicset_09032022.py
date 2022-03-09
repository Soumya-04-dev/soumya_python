'''dic1 = {'Item1': 45.50, 'Item2': 35 , 'Item3': 41.30, 'Item4': 55 , 'Item5': 24}
list1 = list(dic1.values())
print(list1)
list1.sort(reverse=True)
print(list1)
# sorted list =[55, 45.5, 41.3, 35, 24]
for i in range(3):
    for key in dic1:
        if list1[i] == dic1[key]:
            print(key, list1[i])


for key in dic1:
    for i in range(3):
        if dic1[key]==list1[i]:
            print(key,list1[i])
            break
            '''
# sorted_tuples = sorted(dic1.items(), key=lambda item: item[1], reverse=True)
# print(sorted_tuples)
# _______________________________________________________________________________________________
'''
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#output: list2 = [1,2,3,4,5,6,7,8,9,10,11,12]

list2 = []
for i in list1:
    list2.extend(i)
print(list2)
'''
# ___________________________________________________________________________________

# to count the number of given sublist
'''
list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# output --dic1 = {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

dic1 = {}
for i in list1:
    dic1[tuple(i)] = list1.count(i)
print(dic1)

'''
