n = int(input())
v = n
v *= v
for i in range(n):
    key = (n * n) - ((n - i) * (n - i))
    for j in range(key):
        print("",end=" ")
    for j in range(v - key):
        print("*", end="")
    print()