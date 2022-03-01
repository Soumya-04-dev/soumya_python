
#convert string to list

#user_input = input()
#list1 = user_input.split(" ")
#print(list1)
#list(user_input)
#print(list(user_input))

#convert list to string

#user_input= input()
#list1 = "".join(user_input.split(" ") )
#list1 = "".join(list1)
#print(list1)

#to check no of occurences
user_input = input()
list1 = user_input.split(" ")
print(list1)

for list_index in range(0,len(list1)):
    list1[list_index] = int(list1[list_index])
print(list1)
 
user_input01_int = input()
count = 0
for value in list1:
    if int(user_input01_int) == value:
        count = count +1
print(count)