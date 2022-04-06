# to draw a circle of squares using turtle
# fibonacci using recursion- using function
import time
import  datetime
'''
import turtle
squ = turtle.Turtle()
for i in range(4):
    squ.forward(50)
    squ.right(90)
    squ.circle(50)
turtle.done()
'''

'''
n = int(input())

first = 0
second = 1
while True:
    print(first)
    print(second)
    for i in range(0, 20):
        c = first + second
        first = second
        second = c


'''


#Linear search using function
#l1 = [4, 2, 7, 1, 8, 3, 6]
def linear(n, l4):
    for i in range(len(l4)):
        if int(n) == l4[i]:
            return n, i

    return -1

x = datetime.datetime.now()
print(x)

n = int(input())
l4 = [4, 2, 7, 1, 8, 3, 6]
a = linear(n, l4)
if a == -1:
    print("Element not found")
else:
    print(a)
y = datetime.datetime.now()
print(y)

diff = y - x
print(diff.total_seconds())

# Binary search using function


# [11, 21, 31, 41, 61, 71, 81]
# n = int(input())
'''
def binary_search(n, l1):
    for i in range(len(l1)):
        first = 0
        last = len(l1) - 1
        mid = int((first + last)/2)
    while first <= last:
        if n < l1[mid]:
            last = mid - 1
        if n == l1[mid]:
            return mid, l1[mid]-1
            break
        if n > l1[mid]:
            first = mid + 1
        mid = int((first + last) / 2)
    if first > last:
        return -1


x = datetime.datetime.now()
print(x)

#l1 = [41, 21, 71, 11, 81, 31, 61]
l1 = list(range(2400000))
#l1.sort()
n = int(input())
a = binary_search(n, l1)
if a == -1:
    print("Element not found")
else:
    print(a)
y = datetime.datetime.now()
print(y)
diff = y - x
print(diff.total_seconds())
'''

















'''

# display all integers within the range of 100 to 200 having sum of digits is even number.
# to implement linear search and to do binary search
# list1 = [4,2,7,1,8,3,6], take input and find the number with position
# to implement calculator to do basic operations--number from user, take operations from user
# to draw a circle of squares using turtle
# fibonacci using recursion- using function

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
#l1 = [4, 2, 7, 1, 8, 3, 6]
l4 = list(range(24000))
n = input()
for i in range(len(l4)):
    if int(n) == l4[i]:
        print(i, n)
        exit()
print("Element not found")

# binary search

l1 = [41, 21, 71, 11, 81, 31, 61]
l1.sort()
print(l1)  # [11, 21, 31, 41, 61, 71, 81]
# n = int(input())
for i in range(len(l1)):
    first = 0
    last = len(l1) - 1
    mid = int((first + last)/2)
print(l1[mid])

n = int(input())
while first <= last:
    if n < l1[mid]:
        last = mid - 1
    if n == l1[mid]:
        print(mid, l1[mid])
        break
    if n > l1[mid]:
        first = mid + 1
    mid = int((first + last) / 2)

if first > last:
    print("Element not found")
'''

