def split_and_join(line):
    # write your code here
    resultpass = line.split(" ")
    # resultpass = "-".join(line.split(" "))
    resultpass = ("-").join(resultpass)
    return resultpass
    #return   "-".join(line.split(" "))  
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


  #You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.  

'''>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']

>>> a = "-".join(a)
>>> print a
this-is-a-string '''

