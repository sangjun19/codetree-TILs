n = int(input())

# Please write your code here.

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 2
        continue
    if i == 2:
        dp[i] = 7
        continue

    dp[i] = dp[i - 1] * 3 + dp[i - 2] - dp[i - 3]

print(dp[n])