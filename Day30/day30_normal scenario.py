# display all integers within the range of 100 to 200 having sum of digits is even number.
# to implement linear search and to do binary search
# list1 = [4,2,7,1,8,3,6], take input and find the number with position
# to implement calculator to do basic operations--number from user, take operations from user
# to draw a circle of squares using turtle
# fibonacci using recursion- using function
'''
# summation 1.

for i in range(100, 104):
    digit_sum = 0
    n = i
    while n != 0:
        d = n % 10
        digit_sum = digit_sum + d
        n = n // 10
    if digit_sum % 2 == 0:
        print(i)


for i in range(100, 201):
    digit_sum = 0
    x = str(i)
    for j in x:
        digit_sum = digit_sum + int(j)
    if digit_sum % 2 == 0:
        print(i)

# linear search
l1 = [4, 2, 7, 1, 8, 3, 6]
n = input()
for i in range(len(l1)):
    if int(n) == l1[i]:
        print(i, n)
        exit()
print("Element not found")
'''
# binary search

l1 = [41, 21, 71, 11, 81, 31, 61]
l1.sort()
print(l1)  # [11, 21, 31, 41, 61, 71, 81]
# n = int(input())
for i in range(len(l1)):
    lower = 0
    higher = len(l1) - 1
    mid = lower + (higher - lower) // 2
print(l1[mid])

n = int(input())
if n == l1[mid]:
    print(n, mid)
if n < l1[mid]:
    for j in l1[mid]:
        if n == j:
            print(mid, j)
