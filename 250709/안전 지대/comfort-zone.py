n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 0

def dfs(y, x, visited, k):
    for i in range(4):
        dy = y + dir[i][0]
        dx = x + dir[i][1]

        if dy < 0 or dy >= n or dx < 0 or dx >= m:
            continue
        
        if grid[dy][dx] <= k:
            continue
        
        if (dy, dx) in visited: continue

        visited.append((dy, dx))
        dfs(dy, dx, visited, k)

    return 0

min_k = min(min(row) for row in grid)
max_k = max(max(row) for row in grid)
result = [0] * max_k

for l in range(min_k, max_k):
    visited = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > l and (i, j) not in visited:
                cnt += 1
                visited.append((i, j))
                dfs(i, j, visited, l)
    result[l] = cnt

max_k = max(result)
print(result.index(max_k), max_k)

        