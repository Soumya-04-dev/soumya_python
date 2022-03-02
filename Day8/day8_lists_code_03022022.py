import os
import sys

print(os.getcwd())
#print(os.listdir('/'))
#dir_names = os.listdir('/')
#print(dir_names)
#if 'swapfile' in dir_names:
#    print("Swap file exists")

#import-- its a keyword
#os-- its a module/library
#help.mkdir()

for i in range(5):
    os.mkdir('test' + str(i))
