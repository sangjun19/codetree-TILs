N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
chickenNum = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])
            chickenNum += 1            

def dist():
    cnt = 0
    for i in range(len(house)):
        temp = float('inf')
        for j in range(chickenNum):
            if chicken[j][0] == -1: 
                continue
            temp = min(temp, abs(house[i][0]-chicken[j][0]) + abs(house[i][1]-chicken[j][1]))
        cnt += temp
    return cnt

result = float('inf')

def brute(idx, dep):
    global chicken, result
    if chickenNum - dep == M:
        result = min(result, dist())
        return
    for i in range(idx, chickenNum):        
        ty = chicken[i][0]
        tx = chicken[i][1]
        chicken[i][0] = -1
        chicken[i][1] = -1
        brute(i + 1, dep + 1)
        chicken[i][0] = ty
        chicken[i][1] = tx

brute(0, 0)
print(result)