result = []

def dfs(arr, visited, start, cnt):    
    global result
    cnt += 1
    visited.append(start)
    for i in range(len(arr)):
        if arr[i][0] == start and arr[i][1] not in visited:
            dfs(arr, visited, arr[i][1], cnt)
            result.append(cnt)
            visited.pop()
        elif arr[i][1] == start and arr[i][0] not in visited:
            dfs(arr, visited, arr[i][0], cnt)
            result.append(cnt)
            visited.pop()
    return

def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    dfs(arr, [], 1, 0)
    print(result[0])
    
if __name__ == "__main__":
    main()