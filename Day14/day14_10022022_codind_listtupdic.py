list1 = ["sos", "Sohil", "Anjali", "Ishu", "yoga"]
# output: dic = {key = name of strings and value is len of strings} dic = {name:[len,capital letters, small letters]}
dic1 = {}
for string1 in list1:
    dic2 = {}
    is_palindrome = 'yes'
    str_len = len(string1)
    if string1 != string1[:: -1]:
        is_palindrome = 'no'
    count1 = 0
    count2 = 0
    for char1 in string1:
        if char1.isupper():
            count1 = count1 + 1
        if char1.islower():
            count2 = count2 + 1
        dic2[char1] = string1.count(char1)

    # print(dic2)
    #    dic1[string1]=[str_len,count1,count2,dic2]
    # print(dic1)

    dic1[string1] = (str_len, count1, count2, is_palindrome, dic2)
print(dic1)
