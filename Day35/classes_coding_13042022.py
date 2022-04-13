import datetime
import time


class Person:

    def __init__(self, name, surname, phone, birthday_date):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday_date = birthday_date
        self.last_calculated_day_time = None

    def calculate_age(self):
        if self.last_calculated_day_time is None or self.last_calculated_day_time > datetime.datetime.now().strftime(
                '%M'):
            today = datetime.date.today()
            age = today.year - self.birthday_date.year
            self.last_calculated_day_time = datetime.datetime.now().strftime('%M')
            print(self.last_calculated_day_time)
            return age


person = Person("Soumya", "Mohanty", "8390562229", datetime.date(1990, 5, 30))
print(person.calculate_age())

'''
    def calculate_age(self):
        if self.last_calculated_day is None or self.last_calculated_time > datetime.date.today().strftime('%a'):
            today = datetime.date.today()
            age = today.year - self.birthday_date.year
            self.last_calculated_day = datetime.date.today().strftime('%a')
            print(self.last_calculated_day)
            return age
'''
