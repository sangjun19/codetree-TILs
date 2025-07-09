n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(start_y, start_x, visited, k):
    stack = [(start_y, start_x)]
    
    while stack:
        y, x = stack.pop()
        
        for i in range(4):
            dy = y + dir[i][0]
            dx = x + dir[i][1]

            if dy < 0 or dy >= n or dx < 0 or dx >= m:
                continue
            
            if grid[dy][dx] <= k:
                continue
            
            if (dy, dx) in visited:
                continue

            visited.add((dy, dx))
            stack.append((dy, dx))

min_k = min(min(row) for row in grid)
max_k = max(max(row) for row in grid)
result = [0] * max_k

for l in range(1, max_k):
    visited = set()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > l and (i, j) not in visited:
                cnt += 1
                visited.add((i, j))
                dfs(i, j, visited, l)
    
    result[l - 1] = cnt

max_count = max(result)
best_k = result.index(max_count) + 1
print(best_k, max_count)