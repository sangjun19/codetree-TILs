def dp(n, m, item, wall):
    ret = [[[0 for _ in range(1 << len(item))] for _ in range(m)] for _ in range(n)]
    ret[0][0][0] = 1
    
    for y in range(n):
        for x in range(m):
            for mask in range(1 << len(item)):
                if ret[y][x][mask] == 0:
                    continue
                for dy, dx in [(0, 1), (1, 0)]:
                    ny, nx = y + dy, x + dx
                    if ny < n and nx < m and (ny, nx) not in wall:
                        new_mask = mask
                        if (ny, nx) in item:
                            new_mask |= 1 << item.index((ny, nx)) # 몇 번째 아이템인지 찾아서 비트마스크로 표현
                        ret[ny][nx][new_mask] += ret[y][x][mask] # 가능한 경우의 수를 누적
                        ret[ny][nx][new_mask] %= 1000000007
                        
    return ret[n - 1][m - 1][(1 << len(item)) - 1]
    
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
    print(dp(n, m, item, wall))

if __name__ == "__main__":
    main()