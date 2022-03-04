from collections import Counter

tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 2, 4, 4, 4, 4, 8, 8, 8)
print(len(tup1))

count = 0
dict = {}
for i in tup1:
    dict[i] = tup1.count(i)
print(dict)
