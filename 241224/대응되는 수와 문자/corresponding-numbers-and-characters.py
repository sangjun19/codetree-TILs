n, m = map(int, input().split())

d = {}
for i in range(n):
    word = input()
    d[word] = i + 1

for i in range(m):
    index = input()
    if index.isalpha():
        print(d[index])
    else:
        for k, v in d.items():
            if v == int(index):
                print(k)
                break