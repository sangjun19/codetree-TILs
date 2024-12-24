d = {}
n = int(input())
for i in range(n):
    cmd = list(input().split())

    if cmd[0] == "add":
        d[cmd[1]] = cmd[2]
    elif cmd[0] == "remove":
        d.pop(cmd[1])
    elif cmd[0] == "find":
        if cmd[1] in d:
            print(d[cmd[1]])
        else:
            print("None")