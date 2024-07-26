k, n = map(int, input().split())

def back(cnt, result):
    if cnt == n:
        print(' '.join(map(str, result)))
        return
    for i in range(1, k + 1):
        result.append(i)
        back(cnt + 1, result)
        result.pop()

arr = []
back(0, arr)