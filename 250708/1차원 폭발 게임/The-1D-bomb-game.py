n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.

while True:
    flag = True
    stack = []
    for x in numbers:
        if stack and stack[-1][0] == x:
            v, c = stack.pop()
            stack.append((v, c + 1))
            # flag = False
        else:
            if stack and stack[-1][1] >= m:
                stack.pop()
                flag = False

            stack.append((x, 1))
    
    if stack and stack[-1][1] >= m:
        stack.pop()
    if flag:
        break
    numbers = []
    for v, c in stack:
        numbers.append(v)

    

ans = []
for v, c in stack:
    if c > 1: continue
    ans.extend([v] * c)

print(len(ans))
for a in ans:
    print(a)