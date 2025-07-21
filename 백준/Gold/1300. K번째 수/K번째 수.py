def count_less_equal(x, n):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(x // i, n)
    return cnt

def find_kth_number(n, k):
    left, right = 1, k  # k보다 클 필요 없음
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(mid, n) >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

# 입력
n = int(input())
k = int(input())

# 출력
print(find_kth_number(n, k))
