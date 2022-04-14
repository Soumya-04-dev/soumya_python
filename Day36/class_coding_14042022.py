import datetime


class Person:

    def __init__(self, name, surname, birthdate, email, phone):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
        self.phone = phone

    def __str__(self):
        return "%s %s , born: %s\nEmail: %s\nphone: %s " % (
        self.name, self.surname, self.birthdate, self.email, self.phone)


person = Person("Soumya",
                "Mohanty",
                datetime.date(1992, 4, 30),
                "soumya.cric4@gmail.com",
                "8390562229")
print(person)

'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)

    @fullname.setter
    def fullname(self, value):
        # this is much more complicated in real life
        name, surname = value.split(" ", 1)
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname


jane = Person("Jane", "Smith")
print(jane.fullname)

jane.fullname = "Jane Doe"
print(jane.fullname)
print(jane.name)
print(jane.surname)
'''

'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return "%s %s" % (self.name, self.surname)


jane = Person("Jane", "Smith")

print(dir(jane))

'''
