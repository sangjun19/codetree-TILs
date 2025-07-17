INF = float('inf')
v, e = map(int, input().split())
dist = [[INF] * (v + 1) for _ in range( v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                
answer = INF
for i in range(1, v + 1):
    answer = min(answer, dist[i][i])
    
if answer == INF:
    print(-1)
else:
    print(answer)