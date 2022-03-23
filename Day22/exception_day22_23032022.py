'''try:
    a = int(input('Please enter a value'))
    b = int(input('Please enter a value'))
    if b == 0:
        raise ArithmeticError(f'This should not execute as b cant be zero')
        print("Test the values")
    else:
        print('a/b', a/b)
except Exception as ex:
    print("The value of b can't be zero" + '\n' + str(ex))
'''

a = input()
b = input()

try:
    print(int(a) / int(b))

except ZeroDivisionError as ex:
    print("ErrorCode:", ex)

except ValueError as ex1:
    print("ErrorCode:", ex1)
