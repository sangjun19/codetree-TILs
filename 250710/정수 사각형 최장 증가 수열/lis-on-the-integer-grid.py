n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 메모이제이션을 위한 DP 배열
dp = [[-1 for _ in range(n)] for _ in range(n)]

# DFS + 메모이제이션으로 최대 경로 길이 계산
def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = 1  # 현재 위치 자체의 길이
    
    # 4방향 탐색
    for dy, dx in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        y = dy + i
        x = dx + j
        
        # 경계 체크
        if y < 0 or y >= n or x < 0 or x >= n:
            continue
        
        # 증가하는 경로인지 확인
        if grid[y][x] > grid[i][j]:
            dp[i][j] = max(dp[i][j], dfs(y, x) + 1)
    
    return dp[i][j]

# 모든 위치에서 시작하는 경로 중 최대값 찾기
result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)