n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[-1 for _ in range(n)] for _ in range(n)]

def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 1
    
    for dy, dx in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        ty = y + dy
        tx = x + dx
        
        if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
        if grid[y][x] >= grid[ty][tx]: continue

        dp[y][x] = max(dp[y][x], dfs(ty, tx) + 1)
    
    return dp[y][x]

result = 0

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)