n, m = map(int, input().split())
arr = list(map(int, input().split()))
num = list(map(int, input().split()))

d = {}
for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

for i in range(len(num)):
    if num[i] in d:
        print(d[num[i]], end=" ")
    else:
        print(0, end=" ")