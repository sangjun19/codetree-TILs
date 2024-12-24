n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = {}

for n in arr:
    d[n] = 1

cnt = 0;
for key, value in d.items():
    dif = k - key
    if dif in d and dif != key:
        cnt += 1

print(cnt//2)