'''n = input()
sub = input()
count = 0
for index in range(0, len(n)):
    temp_str = n[index:index+len(sub)]
    if temp_str == sub:
        count = count + 1
print(count)
'''
s = input()
if s.isalnum():
    print(True)
else:
    print(False)
if s.isalpha():
    print(True)
else:
    print(False)
if s.isdigit():
    print(True)
else:
    print(False)
if s.islower():
    print(True)
else:
    print(False)
if s.isupper():
    print(True)
else:
    print(False)
