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
    dif = k - key
    if dif not in d:
        continue
    if dif == key:
        cnt += value * (value - 1)
    else:
        cnt += value * d[dif]

print(cnt//2)