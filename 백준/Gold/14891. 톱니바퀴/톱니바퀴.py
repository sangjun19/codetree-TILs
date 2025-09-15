arr = [[0 for _ in range(8)] for _ in range(4)]
for i in range(4):
    temp = list(input())
    for j in range(8):
        arr[i][j] = int(temp[j])
    
K = int(input())

for i in range(K):
    N, D = map(int, input().split())
    N -= 1
    move = [0] * 4
    
    move[N] = D
    
    for i in range(N+1, 4):
        if arr[i-1][2] != arr[i][6]:
            move[i] = -move[i-1]
        else:
            break

    for i in range(N-1, -1, -1):
        if arr[i+1][6] != arr[i][2]:
            move[i] = -move[i+1]
        else:
            break
    
    for i in range(4):
        if move[i] == 1:
            arr[i].insert(0, arr[i].pop())
        elif move[i] == -1:
            arr[i].append(arr[i].pop(0))

print(arr[0][0] + arr[1][0]*2 + arr[2][0]*4 + arr[3][0]*8)    