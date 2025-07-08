n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

dir = [[0, 0], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1],]
ret = 0
q = []
q.append((r - 1, c - 1, 0))

while q:
    y, x, count = q.pop(0)
    # print(y, x, count)
    ret = max(count, ret)    
    for i in range(1, n):
        ty, tx = dir[move_dir[y][x]]
        ty *= i
        tx *= i
        dy, dx = y + ty, x + tx
        if dy < 0 or dy >= n or dx < 0 or dx >= n:
            continue
        if num[dy][dx] <= num[y][x]:
            continue
        q.append((dy, dx, count + 1))

print(ret)