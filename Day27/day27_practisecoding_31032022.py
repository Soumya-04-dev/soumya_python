'''list1 = input().split()
list2 = input().split()
print(list1)
print(list2)

for i in list1:
    for j in list2:
        a = int(i), int(j)
        print(a, end=" ")
'''
from collections import Counter

no_of_shoes = int(input())
shoe_sizes = input().split()
no_of_customers = int(input())
list3 = []
for i in range(no_of_customers):
    shoe_size, price = input().split()
    list3.append((shoe_size, price))
print(list3)
amount_list = []
for j in list3:
    if j[0] in shoe_sizes:
        amount_list.append(int(j[1]))
        shoe_sizes.remove(j[0])

print(sum(amount_list))

# no_of_customers = int(input())
# shoe_size, price = input().split
