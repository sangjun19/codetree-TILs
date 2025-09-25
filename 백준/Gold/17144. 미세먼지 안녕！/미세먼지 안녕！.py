import copy

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

def diffusion():
    global arr
    temp = [[0 for _ in range(C)] for _ in range(R)]    
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1: temp[i][j] = -1
            if arr[i][j] <= 0: continue
            q = []
            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                y = i + dy
                x = j + dx
                if y < 0 or y >= R or x < 0 or x >= C:
                    continue
                if arr[y][x] == -1:
                    continue
                q.append((y, x))
                
            num = len(q)
            if num == 0: continue
            
            while q:
                y, x = q.pop()
                temp[y][x] += arr[i][j] // 5
            temp[i][j] += arr[i][j] - ((arr[i][j] // 5) * num)
            
    arr = copy.deepcopy(temp)
    
def air():
    global arr
    for i in range(R):
        if arr[i][0] != -1: continue
        for j in range(i - 2, -1, -1):
            arr[j+1][0] = arr[j][0]
        for j in range(1, C):
            arr[0][j-1] = arr[0][j]
        for j in range(1, i + 1):
            arr[j-1][C-1] = arr[j][C-1]
        for j in range(C-2, 0, -1):
            arr[i][j+1] = arr[i][j]
        arr[i][1] = 0
        i += 1
        for j in range(i + 2, R):
            arr[j-1][0] = arr[j][0]
        for j in range(1, C):
            arr[R-1][j-1] = arr[R-1][j]
        for j in range(R - 2, i - 1, -1):
            arr[j+1][C-1] = arr[j][C-1]
        for j in range(C-2, 0, -1):
            arr[i][j+1] = arr[i][j]
        arr[i][1] = 0
        return
        
    return

for k in range(T, -1, -1):
    if k == 0:
        sum = 2
        for i in range(R):
            for j in range(C):
                sum += arr[i][j]
        print(sum)
    else:
        diffusion()
        air()