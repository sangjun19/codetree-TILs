n = int(input())
coin = []
for i in range(n):
    coin.append(list(map(int, input().split())))
max_coin = 0
for i in range(n - 2):
    for j in range(n - 2):
        sum = 0
        for k in range(3):
            for l in range(3):
                if coin[i + k][j + l] == 0:
                    continue
                sum += 1
        max_coin = max(sum, max_coin)
print(max_coin)