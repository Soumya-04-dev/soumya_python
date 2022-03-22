'''fo = open('test1.txt', 'w')
fo.write("testing the file input output scenario")
fo.close()
'''
# a mode is for append
# w mode is for write
# r mode is for read only

fo = open('test1.txt', 'a')
for i in range(0, 30):
    fo.write("My name is Soumya" + str(i) + '\n')

fo.close()
