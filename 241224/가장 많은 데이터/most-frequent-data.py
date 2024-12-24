n = int(input())
d = {}
maxN = 0
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
    maxN = max(maxN, d[word])

print(maxN)