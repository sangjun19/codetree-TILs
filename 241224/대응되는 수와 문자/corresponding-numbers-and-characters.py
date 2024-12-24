n, m = map(int, input().split())

d = {}
for i in range(n):
    word = input()
    d[word] = i + 1
    d[str(i + 1)] = word

for i in range(m):
    index = input()    
    print(d[index])