list1 = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
max_sum = 0
sum_dict = {}
for i in range(0,len(list1)):
    sum_element = sum(list1[i])
    sum_dict[i] = sum_element

max_sum_dict = max(sum_dict.values())
for kev,values in sum_dict.items():
    if values == max_sum_dict:
        print(list1[kev])
        break