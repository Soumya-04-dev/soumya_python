user_input = input("Please enter any number as input")
user_input_list = user_input.split(" ")
sum_int = 0
for i in user_input_list:
    sum_int = int(i) + sum_int
print("The sum total is " + str(sum_int))