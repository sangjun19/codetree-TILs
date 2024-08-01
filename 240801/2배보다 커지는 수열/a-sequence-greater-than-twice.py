cnt = 0

def back(start, end, limit):
    global cnt
    if limit == 0:
        cnt += 1
        return
    if start > end:
        return    
    for i in range(start, end + 1):
        back(i * 2, end, limit - 1)

def main():
    n, m = map(int, input().split())    
    back(1, m, n)
    print(cnt)

if __name__ == "__main__":
    main()