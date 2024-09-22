def main():
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    
    for _ in range(k):
        num = arr[r][c]
        q = []
        visited = []
        max_num = 0
        ci, cx = 0, 0
        for i in range(n):
            for j in range(n):
                if max_num < arr[i][j] and arr[i][j] < num:
                    max_num = arr[i][j]
                    ci, cx = i, j
        q.append((r, c))
        visited.append((r, c))
        while q:
            y, x = q.pop(0)
            if (y, x) == (ci, cx):
                break
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in visited:
                    q.append((ny, nx))
                    visited.append((ny, nx))
        r, c = y, x
    print(r, c)
        

if __name__ == "__main__":
    main()