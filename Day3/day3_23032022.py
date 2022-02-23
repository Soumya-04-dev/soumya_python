name = input("Take a name as input")
count = 0
for i in name:
    count = count + 1
print(count)    
print(len(name))


# nameerror= if name is not defined
#TypeError= 
#ValueError= if extra variable is taken without define the variable: a,b = 1,2,3 
# IndexError= refering the index which is not present in the string
print(count)

name = "22022022"
if name == name[::-1]:
    print("It is a palindrome")

    
