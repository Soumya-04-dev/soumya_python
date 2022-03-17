'''l1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#dic1 = {'harry':37.21, Berry' :37.21}
dic1 ={}
for key in l1:
    dic1[key[0]] = key[1]
min_value = (min(list(dic1.values())))
sorted_dic = sorted(dic1.items(), key=lambda item: item[1], reverse=False)
print(sorted_dic)'''
