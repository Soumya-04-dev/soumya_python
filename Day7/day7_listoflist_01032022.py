list1 = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
max_sum = []
sum_dict = {}
'''
for i in range(0,len(list1)):
    sum_element = sum(list1[i])
    sum_dict[i] = sum_element

max_sum_dict = max(sum_dict.values())
for kev,values in sum_dict.items():
    if values == max_sum_dict:
        print(list1[kev])
        break
    

for list_index1 in range(len(list1)):
    max_sum.append(sum(list1[list_index1]))
print(list1[max_sum.index(max(max_sum))])     


Step 2:
max(l,key=sum)
'''


for l1 in range(len(list1)):
    for l2 in range(l1+1,len(list1)):
        if sum(list1[l1]) > sum(list1[l2]):
            list1[l1],list1[l2] = list1[l2],list1[l1]
print(list1[-1])
