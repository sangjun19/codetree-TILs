def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = sum(arr)
    arr.sort()
    for i in range(1, n):
        result = 0
        for j in range(0, i):
            result += arr[j]
        if ans - result == result:
            print("YES")
            exit()
    print("NO")
            
    
if __name__ == "__main__":
    main()