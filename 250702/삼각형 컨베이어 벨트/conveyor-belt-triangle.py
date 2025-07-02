n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    l.insert(0, d.pop())
    r.insert(0, l.pop())
    d.insert(0, r.pop())

print(*l)
print(*r)
print(*d)