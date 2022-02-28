user_input_list = input("Please enter any number as input " " ").split(" ")
# min(user_input_list)
for i in range(0,len(user_input_list)):
    user_input_list[i] = int(user_input_list[i])
#user_input_list.sort()
#print(user_input_list[0])

small_num = 0
for i in user_input_list:
    if i == min(user_input_list):
        small_num = i
        print(small_num)
