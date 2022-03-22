try:
    a = 1 / 0
    f4 = open('test2.txt', 'w+')
    f4.write("This is my test file for exeception handling")

except IOError:
    print("This is IO error and it Can't find the file or read data")

except ZeroDivisionError:
    print("This is the arithmetic exception ")

else:
    print("File created and No such exception found")
    f4.close()

finally:
    print("Even if exception is there this has to execute")
