user_input = input()
list1 = user_input.split(" ")
print(list1)
for list_element in list1:
    if  (len(list_element) >= 2) and (list_element[0] == list_element[-1]):
        print(list_element)