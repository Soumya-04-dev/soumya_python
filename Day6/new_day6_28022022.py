user_input = input()
list1 = user_input.split(" ")
print(list1)
list_digit= []
list_char = []

#is digit:  digit or not
#is Alpha:  each characters
for list_element in list1:
    if list_element.isdigit():
        list_digit.append(list_element)
    if list_element.isalpha():
        list_char.append(list_element)
print(list_digit)        
print(list_char)