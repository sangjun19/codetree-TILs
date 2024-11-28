n = int(input())
limit = 0
dp = [[0 for _ in range(n + 1)] for _ in range(101)]
energy = [0]
happy = [0]
energy += list(map(int, input().split()))
happy += list(map(int, input().split()))
for i in range(1, 101):
    for j in range(1, n + 1):
        if energy[j] <= i:
            if happy[j] + dp[i - energy[j]][j] > dp[i][j - 1]:
                dp[i][j] = happy[j] + dp[i - energy[j]][j - 1]
                continue

        dp[i][j] = dp[i][j - 1]
# for a in dp:
#     print(*a)
print(dp[100][n])