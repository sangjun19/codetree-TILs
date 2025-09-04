K, N = map(int, input().split())

# Please write your code here.
def back(dep, list):
    global K, N
    if dep == N:
        for i in range(N):
            print(list[i], end=' ')
        print()
        return 0
    for i in range(1, K+1):
        list.append(i)
        back(dep+1, list)
        list.pop()

    return 0

back(0, [])