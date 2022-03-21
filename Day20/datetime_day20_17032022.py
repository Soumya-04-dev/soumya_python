import datetime
import time
from datetime import timezone

# print(datetime.date.today())

today_date = datetime.date.today()
print(today_date)
print(today_date.strftime("%a"))

new_today_date = today_date.strftime("%d/%m/%Y")
print(new_today_date)

# t = time.localtime()
# print(t)
current_time = time.strftime("%H:%M:%S")
print(current_time)

now1 = datetime.datetime.now()
print(now1)
# dd/mm/YY H:M:S
dt_string = now1.strftime("%d%m%Y_%H%M%S")
print("current date and time =", dt_string)

f = open(f'log_{dt_string}', 'w+')

now1 = datetime.datetime.now()
now2 = datetime.datetime.now().astimezone(tz=datetime.timezone.utc)
print(now1)
print(now2)

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=4)  # n=1
print(Previous_Date)

days_ago_date = Previous_Date.strftime("%d/%m/%Y")
print(days_ago_date)
