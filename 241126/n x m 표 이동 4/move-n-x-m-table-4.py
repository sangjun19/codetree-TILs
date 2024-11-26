result = 0

def dfs(y, x, n, m, item, wall, visited, count):
    global result
    if y == n - 1 and x == m - 1 and count == len(item):
        result += 1
        # print(visited)
        return
    for dy, dx in [(0, 1), (1, 0)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in wall and (ny, nx) not in visited:
            visited.append((ny, nx))
            if (ny, nx) in item:
                dfs(ny, nx, n, m, item, wall, visited, count + 1)
            else:
                dfs(ny, nx, n, m, item, wall, visited, count)
            visited.pop()

def main():
    n, m, r, c = map(int, input().split())
    item = []
    wall = []
    for i in range(r):
        a, b = map(int, input().split())
        item.append((a - 1, b - 1))
    for i in range(c):
        a, b = map(int, input().split())
        wall.append((a - 1, b - 1))
    dfs(0, 0, n, m, item, wall, [], 0)
    print(result % 1000000007)

if __name__ == "__main__":
    main()