n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
arr.append(0)
stack = [0]
result = 0

for i in range(1, n + 2):    
    while stack and arr[stack[-1]] > arr[i]:
        height = arr[stack.pop()]
        width = i - stack[-1] - 1
        result = max(result, height * width)
    stack.append(i)
print(result)