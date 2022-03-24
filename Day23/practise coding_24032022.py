import datetime
import calendar

'''
time_str = input("Enter the date format as MM DD YYYY")
#time_str1 = time_str.split(" ")
convert_date = datetime.datetime.strptime(time_str, "%Y %m %d")
print(convert_date)
format_date = convert_date.strftime("%m %d %Y")
print(format_date)
find_day = convert_date.strftime("%A")
print(find_day.upper())

#using calendar
n = input()
mm, dd, yyyy = n.split()
result = calendar.day_name[calendar.weekday(int(yyyy), int(mm), int(dd))].upper()
print(result)'''

# convert lowercase to uppercase and viceversa:
'''
a = "This is Hero"
#a.swapcase()
list1 = []
for i in a:
    if i.isupper():
        convert_lower = i.lower()
        list1.append(convert_lower)
    if i.islower():
        convert_upper = i.upper()
        list1.append(convert_upper)
print("".join(list1))
'''
# convert string to list and change the character of position mentioned and print the string

a = "Soumya"
print(a[5])
list1 = list(a)
print(list1)
for i in list1:
    list1[5] = 'o'
print(list1)
string1 = "".join(list1)
print(string1)
