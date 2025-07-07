n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def mov(y, x_dir, y_dir):
    global a
    if x_dir == 1:
        a[y].insert(0, a[y].pop())
    else:
        a[y].insert(len(a[y]), a[y].pop(0))  

    if y_dir >= 0:
        check(y, 1, x_dir)
    if y_dir <= 0:
        check(y, -1, x_dir)

def check(y, y_dir, x_dir):
    if y != 0 and y_dir < 0:
        for j in range(m):
            if a[y][j] == a[y - 1][j]:
                mov(y - 1, x_dir * -1, -1)
                break

    if y < n - 1 and y_dir > 0:
        for j in range(m):
            if a[y][j] == a[y + 1][j]:
                mov(y + 1, x_dir * -1, 1)
                break

# Please write your code here.
for i in range(q):
    y, temp = winds[i]
    if temp == 'L':
        x = 1
    else:
        x = -1
    mov(y - 1, x, 0)

for i in a:
    print(*i)