import random

random_no = random.randint(1, 20)
while True:
    for rand1 in range(3):
        user_input = int(input("Please enter an number"))
        if user_input == random_no:
            print("User_input matches random no:" + "No of Attempts are : " + str(rand1))
            break

        if user_input > random_no:
            print("The user_input no is more than random no:")

        if user_input < random_no:
            print("The user_input no is less than random no:")

    user_input1 = input("Do you want to continue the game")
    if user_input1 == 'Yes':
        continue
    else:
        break

# print("You have completed your 3 attempts and still the guess is wrong :"
#    + "the random number is :" + str(random_no))
