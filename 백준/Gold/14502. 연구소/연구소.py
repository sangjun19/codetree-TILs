import collections
import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

virus_list = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus_list.append((i, j))

def bfs():
    temp_arr = copy.deepcopy(arr)
    q = collections.deque(virus_list)
    
    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and temp_arr[ny][nx] == 0:
                temp_arr[ny][nx] = 2
                q.append((ny, nx))
    
    safe_count = 0
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 0:
                safe_count += 1
    
    return safe_count


def make_wall(wall_count, start):
    global result
    
    if wall_count == 3:
        result = max(result, bfs())
        return

    for i in range(start, n * m):
        r = i // m
        c = i % m
        
        if arr[r][c] == 0:
            arr[r][c] = 1

            make_wall(wall_count + 1, i + 1)
            arr[r][c] = 0

make_wall(0, 0)
print(result)