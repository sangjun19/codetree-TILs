from queue import PriorityQueue

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    arr[y-1][x-1] = -1
    
L = int(input())
pq = PriorityQueue()
for _ in range(L):
    n, d = input().split()
    pq.put((int(n), d))

cnt, len = -1, 1
y, x, d = 0, 0, 1
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
nc, nd = pq.get()
arr[y][x] = 0

while True:
    if y < 0 or y >= N or x < 0 or x >= N:
        break
    if cnt - len < arr[y][x] and arr[y][x] != 0:
        break
    
    if arr[y][x] == -1: len += 1
    
    cnt += 1
    arr[y][x] = cnt
    
    if nc == cnt:
        if nd == "L": d = (d+3)%4
        if nd == "D": d = (d+1)%4
        
        if not pq.empty():
            nc, nd = pq.get()
        else:
            nc = -1
        
    y += dir[d][0]
    x += dir[d][1]

print(cnt+1)
# for a in arr:
#     print(*a)