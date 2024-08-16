def main():
    n = int(input())
    arr = []
    for _ in range(n):
        x1, x2 = map(int, input().split())
        arr.append((x1, x2))
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            px1, px2 = arr[j]
            x1, x2 = arr[i]
            if x1 > px2 or x2 < px1:
                dp[i] += 1
    print(max(dp))
            
    
if __name__ == "__main__":
    main()