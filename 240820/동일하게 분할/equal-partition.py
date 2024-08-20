def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = sum(arr)
    arr.sort()
    for i in range(n):
        result = 0
        for j in range(i, n):
            result += arr[j]
            if ans - result == result:
                print("Yes")
                exit()        
    print("No")
            
    
if __name__ == "__main__":
    main()