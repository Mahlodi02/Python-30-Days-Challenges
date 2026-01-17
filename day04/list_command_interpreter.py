# List Command Interpreter

list = []
N = int(input("How many action you want to make/operate in a list: "))


for _ in range(N):
    command = input().split()
    action = command[0]
        
    if action == "insert":
        index = int(command[1])
        value = int(command[2])
        list.insert(index, value)
        
    elif action == "append":
        value = int(command[1])
        list.append(value)
        
    elif action == "remove":
        value = int(command[1])
        list.remove(value)
        
    elif action  == "sort":
        list.sort()
        
    elif action == "pop":
        list.pop()
        
    elif action == "reverse":
        list.reverse()
        
    elif action == "print":
            print(list)


    

