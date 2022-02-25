if __name__ == '__main__':
    N = int(input())
    l1 = []
    for i in range(N):
        userinput = input()
        cmd_list = userinput.split(" ")
        if cmd_list[0] == 'insert':
            l1.insert(int(cmd_list[1]),int(cmd_list[2]))  
        if cmd_list[0] == 'append':
            l1.append(int(cmd_list[1]))
        if cmd_list[0] == 'remove':
            l1.remove(int(cmd_list[1]))
        if cmd_list[0] == 'sort':
            l1.sort()
        if  cmd_list[0] == 'pop':
            l1.pop()   
        if  cmd_list[0] == 'reverse':
            l1.reverse()                 
        if  cmd_list[0] == 'print':
            print(l1) 