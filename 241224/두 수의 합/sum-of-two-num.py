n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = {}

for n in arr:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

cnt = 0;
for key, value in d.items():
    for i in range(value):
        dif = k - key
        if dif in d:
            cnt += d[key]
        if dif == key:
            cnt -= 1

print(cnt//2)