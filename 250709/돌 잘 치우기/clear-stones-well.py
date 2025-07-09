from itertools import combinations
from collections import deque

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

q = deque()
for i in range(k):    
    grid[r[i]][c[i]] = 2
    q.append((r[i], c[i]))

while q:
    y, x = q.popleft()
    for dy, dx in dir:
        ty = y + dy
        tx = x + dx
        if ty < 0 or ty >= n or tx < 0 or tx >= n: 
            continue
        if grid[ty][tx] != 0: 
            continue
        grid[ty][tx] = 2
        q.append((ty, tx))

initial_water = sum(row.count(2) for row in grid)

stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))

def bfs_from_stones(stone_positions):
    temp_grid = [row[:] for row in grid]
    
    for y, x in stone_positions:
        temp_grid[y][x] = 2
    
    q = deque(stone_positions)
    
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ty = y + dy
            tx = x + dx
            if ty < 0 or ty >= n or tx < 0 or tx >= n:
                continue
            if temp_grid[ty][tx] != 0:
                continue
            temp_grid[ty][tx] = 2
            q.append((ty, tx))
    
    return sum(row.count(2) for row in temp_grid)


ans = initial_water
for comb in combinations(stones, m):
    result = bfs_from_stones(comb)
    ans = max(ans, result)

print(ans)