# f1 = open('test1.txt', 'r')
# contains = f1.read()
# print(contains)
'''
f1 = open('test1.txt', 'r')
contains = f1.readlines()
print(contains)
f1.close()
f2 = open('test1.txt', 'w+')
for line in contains:
    up_case = line.upper()
    f2.write(up_case)
f2.close()'''

f3 = open('test1.txt', 'r')
# f3.readline()
# print(f3.readline())
line = f3.readline()
print(line)
while line:
    line = f3.readline()
    print(line)
