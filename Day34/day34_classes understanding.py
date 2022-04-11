import datetime

dict1 = {'name': 'Sohil', 'age': 15, 'phone': '9776151317'}


class Person:

    def __init__(self, name, surname, birthdate, phone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.phone = phone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(self.birthdate.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age


person = Person('Soumya', 'Mohanty', datetime.date(2022, 4, 11), '8390562229', 'soumya.cric4@gmail.com')
print(person.name)
print(person.age())

# for i in ['name', 'age', 'phone', 'month']:
# if hasattr(person, i):
#     print("Attribute exists" + i)
# if getattr(person, i):
#    print("getAttribute" +i)
for i in dict1:
    setattr(person, i, dict1[i])

person.name = 'Anjali'
print(person.name)
print(person.phone)

'''

import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(2022, 3, 10), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())
'''
