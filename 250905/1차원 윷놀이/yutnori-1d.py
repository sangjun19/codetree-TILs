n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
result = 0
def back(player, dep):
    global result
    if dep == n:
        cnt = 0
        # print(*player)
        for p in player:
            if p >= m: cnt += 1
        result = max(cnt, result)
        return
    for i in range(len(player)):
        player[i] += nums[dep]
        back(player, dep + 1)
        player[i] -= nums[dep]

back([1] * k, 0)
print(result)