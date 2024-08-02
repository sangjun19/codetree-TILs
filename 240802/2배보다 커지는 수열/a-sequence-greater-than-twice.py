def main():
    global result
    result = 0
    
    def dp(pos, count):   
        global result     
        if times[pos] > n - count or times[pos] == 0:
            return
        if n - count == 1: # 끝나기 직전
            result += outcomes[pos]
            return
        for i in range(pos * 2, m + 1):
            dp(i, count + 1)
    
    n, m = map(int, input().split())    
    outcomes = [0] * (m + 1)
    times = [0] * (m + 1)
    
    for i in range(m // 2, 0, -1):
        outcomes[i] = m - i * 2 + 1
        times[i] = times[i * 2] + 1
        
    for i in range(1, m + 1):
        if times[i] >= n - 1:
            dp(i, 1)
            
    print(result)
    # print(outcomes)
    # print(times)
    

if __name__ == "__main__":
    main()