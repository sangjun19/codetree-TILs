def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0, sum(arr)]
    # print(dp)
    for i in range(0, n):
        dp[0] += arr[i]
        dp[1] -= arr[i]
        if dp[0] == dp[1]:
            print("YES")
            exit()
            
    print("NO")
    
if __name__ == "__main__":
    main()