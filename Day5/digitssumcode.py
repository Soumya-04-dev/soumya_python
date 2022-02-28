user_input = input("Please enter any number as input " " ")
user_input_list = user_input.split(" ")
output_list = []
for i in user_input_list:
    sum_int = 0
    for data in i:
        sum_int = int(data) + sum_int
    output_list.append(str(sum_int))
print(output_list)   


# q = list(map(lambda ele: sum(int(sub) for subn in str(ele)), test_list))
# index purpose: need to use range function for i in range(0,5)
# values: then we can directly use for i in N

