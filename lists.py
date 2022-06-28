N = int(input())
new_list = []

for i in range(N):
    res = input().split()
    command = res[0]
    args = res[1:]
    
    if command == "insert":
        new_list.insert(int(args[0]), int(args[1]))
    elif command == "remove":
        new_list.remove(int(args[0]))
    elif command == "append":
        new_list.append(int(args[0]))
    elif command == "sort":
        new_list.sort()
    elif command == "pop":
        new_list.pop()
    elif command == "reverse":
        new_list.reverse()
    else:
        print(new_list)
            