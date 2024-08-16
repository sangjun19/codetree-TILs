def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * n
    dp_s = [1] * n
    for i in range(1, n):        
        for j in range(0, i):
            status = dp_s[j]
            if status == 1:
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)            
            if arr[i] < arr[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    dp_s[i] = 0
    
    # print(dp)
    print(max(dp))

if __name__ == "__main__":
    main()