n = int(input())

# Please write your code here.
def check(arr):
    cnt = 1
    for i in range(0, n - 1):
        if arr[i] == 1 or arr[i] == cnt:
            cnt = 1
            continue
        if arr[i] != arr[i+1]:
            return False
        cnt += 1
    
    if arr[n-1] != cnt: return False
    return True

result = 0

def back(arr, dep):
    global result
    if dep == n:
        if check(arr) == 1: 
            # print(*arr)
            result += 1
        return

    for i in range(1, 4):
        arr.append(i)
        back(arr, dep+1)
        arr.pop()

back([], 0)
print(result)