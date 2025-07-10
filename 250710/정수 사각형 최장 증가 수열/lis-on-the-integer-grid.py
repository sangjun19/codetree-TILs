n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[0 for _ in range(n)] for _ in range(n)]

arr = set()

for i in range(n):
    for j in range(n):
        arr.add(grid[i][j])
        if grid[i][j] != 1: continue
        dp[i][j] = 1

arr = sorted(arr)
arr.pop(0)
result = 0

for a in arr:
    for i in range(n):
        for j in range(n):
            if grid[i][j] != a:
                continue
            for dy, dx in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                y = dy + i
                x = dx + j
                if y < 0 or y >= n or x < 0 or x >= n:
                    continue
                if a <= grid[y][x]:
                    continue
                dp[i][j] = max(dp[i][j], dp[y][x] + 1)
                result = max(dp[i][j], result)

# for d in dp:
#     print(*d)
print(result)