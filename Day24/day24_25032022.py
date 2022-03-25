'''input_int = int(input("Enter an integer"))
country = input("Enter country name \n")
list1 = []
list1 = country.split(" ")
arrange_data = set(list1)
arrange_data.add(input())
count = 0
for i in arrange_data:
    count = count +1
print(count)

input_int = int(input())
list2 = []
for i in range(input_int):
    country = input()
    list2.append(country)
print(list2)
arrange_data = set(list2)
print(arrange_data)
arrange_data.add(input())
count = 0
for i in arrange_data:
    count = count +1
print(count)
'''
'''

engstudents = int(input())
rollnumber1 = input().split()
for i in range(len(rollnumber1)):
    rollnumber1[i] = int(rollnumber1[i])
print(rollnumber1)
frenchstudents = int(input())
rollnumber2 = input().split()
for j in range(len(rollnumber2)):
    rollnumber2[j] = int(rollnumber2[j])
print(rollnumber2)

arrange_data1 = set(rollnumber1)
arrange_data2 = set(rollnumber2)
test1 = arrange_data1.union(arrange_data2)
print(test1)
count = 0
for i in test1:
    count = count + 1
print(count)

#total = rollnumber1 + rollnumber2
#print(total)
count = 0
arrange_data = set(total)
for i in arrange_data:
    count = count + 1
print(count)

#print(rollnumber1)
#print(rollnumber2)
'''

engstudents = int(input())
rollnumber1 = input().split()
for i in range(len(rollnumber1)):
    rollnumber1[i] = int(rollnumber1[i])
print(rollnumber1)
frenchstudents = int(input())
rollnumber2 = input().split()
for j in range(len(rollnumber2)):
    rollnumber2[j] = int(rollnumber2[j])
print(rollnumber2)

total_set2 = set(rollnumber2)
total_set1 = set(rollnumber1)
intersect = total_set1.intersection(total_set2)
print(intersect)
