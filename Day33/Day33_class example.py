'''
class Parent:
    parent_attr = 100
    print("test1")
    def __init__(self):
        print("parent attribute")

    def get_parent_attr(self):
        print(Parent.parent_attr)

    def set_parent_attr(self, new_parent_attr):
        Parent.parent_attr = new_parent_attr
        print(Parent.parent_attr)



class Child(Parent):

    def __init__(self):
        print("Child Attribute")


a = Parent()
a.get_parent_attr()
a.set_parent_attr(200)
b = Parent()
b.get_parent_attr()
b.set_parent_attr(400)


a = Child()
a.get_parent_attr()
a.set_parent_attr(200)
'''


class JustCounter:
    __secretCount = 0

    def count(self):
        print(JustCounter.__secretCount)
        JustCounter.__secretCount += 1
        print(JustCounter.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# counter1 = JustCounter()
# counter1.count()
# print(counter.__secretCount)
