'''l1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#dic1 = {'harry':37.21, Berry' :37.21}
dic1 ={}
for key in l1:
    dic1[key[0]] = key[1]
min_value = (min(list(dic1.values())))
sorted_dic = sorted(dic1.items(), key=lambda item: item[1], reverse=False)
print(sorted_dic)'''

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
