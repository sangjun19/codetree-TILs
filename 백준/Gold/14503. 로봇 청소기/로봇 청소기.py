n, m = map(int, input().split())
y, x, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    if arr[y][x] == 0:
        arr[y][x] = 2
        result += 1
    
    chk = 0
    for i in range(4):
        d = (d+3)%4
        ny, nx = y+dy[d], x+dx[d]
        # if ny < 0 or ny >= n or nx < 0 or nx >= m:
        #     continue
        if arr[ny][nx] == 0:
            chk = 1
            y, x = ny, nx
            break
        
    if chk: continue
    
    nd = (d+2)%4
    ny, nx = y+dy[nd], x+dx[nd]
    # if ny < 0 or ny >= n or nx < 0 or nx >= m:
    #     break
    if arr[ny][nx] == 1:
        break    
    y, x = ny, nx

print(result)