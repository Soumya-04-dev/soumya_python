name = input("Please enter a string")
for i in range(len(name)):
    if (i%2 == 0):
        print("The even character is " + name[i])
    else:
        print("The odd character is " + name[i])    
           
'''
String is immutable
List is mutuable
python is having membership and identity, 1. Membership: as command we use IN.... for i in name

for i in 5:
... print(i)
  File "<stdin>", line 2
    print(i)
    ^
IndentationError: expected an indented block
>>> for i in 5:
...     print(i)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> string= soumya
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'soumya' is not defined
>>> name = soumya
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'soumya' is not defined
>>> name = "soumya"
>>> name[0]= 'M'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> l=[1,2,3,4,5]
>>> type(l)
<class 'list'>
>>> l1=['sohil','soumya','Anjali']
>>> type(l1)
<class 'list'>
>>> l1[0]
'sohil'
>>> l2[1,'soumya']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l2' is not defined
>>> l2 = [1,'soumya']
>>> l2[1]
'soumya'
>>> l2[0]
1
>>> dir[l2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> dir(l2)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> print(l2)
[1, 'soumya']
>>> print(l2[0])
1
>>> print(l[1:3:1])
[2, 3]
>>> 
KeyboardInterrupt
>>> l4 = [1,2,3,4,5,6,7,8,9,10]
>>> print(len(l4))
10
>>> l4[2] = 11
>>> print(l4)
[1, 2, 11, 4, 5, 6, 7, 8, 9, 10]
>>> l4.append(12)
>>> print(l4)
[1, 2, 11, 4, 5, 6, 7, 8, 9, 10, 12]
>>> l4
[1, 2, 11, 4, 5, 6, 7, 8, 9, 10, 12]
>>> help(l4.append)

>>> help(l4.pop)

>>> type(l4)
<class 'list'>
>>> help(l4.insert)

>>> l4.insert(2,3)
>>> l4
[1, 2, 3, 11, 4, 5, 6, 7, 8, 9, 10, 12]
>>> l4.insert(2,"Soumya")
>>> l4
[1, 2, 'Soumya', 3, 11, 4, 5, 6, 7, 8, 9, 10, 12]
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> l4 == "sohil"
False
>>> sohil in l4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sohil' is not defined
>>> "sohil" in l4
False
>>> len(l4)
13
>>> l5 = [1,2,3,4,5,6,7,8,9,10]
>>> l5[max]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not builtin_function_or_method
>>> dir(l5)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> max(l5)
10
>>> min(l5)
1
>>> l2 = [1,2,3,4,4,5,7,7]
>>> help(count)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> help(l2.count)

>>> count(l2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> l2.count(7)
2
>>> l2.append([3,4,5])
>>> l2
[1, 2, 3, 4, 4, 5, 7, 7, [3, 4, 5]]
>>> type(l2[::-1])
<class 'list'>
>>> l2.insert(2,[3,4,5])
>>> l2
[1, 2, [3, 4, 5], 3, 4, 4, 5, 7, 7, [3, 4, 5]]
>>> l2[0]
1
>>> l2[1]
2
>>> l2[2]
[3, 4, 5]
>>> l2[2][0]
3
>>> l2[9][1]
4
>>> l2[-1][2]
5
>>> help(l2.extend)

>>> l2.extend(3,4,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: extend() takes exactly one argument (3 given)
>>> l2.insert(-1,[4,5,6])
>>> l2
[1, 2, [3, 4, 5], 3, 4, 4, 5, 7, 7, [4, 5, 6], [3, 4, 5]]
>>> l2.extend([2,3,4])
>>> l2
[1, 2, [3, 4, 5], 3, 4, 4, 5, 7, 7, [4, 5, 6], [3, 4, 5], 2, 3, 4]

'''