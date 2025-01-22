n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
cnt = 0
for i in range(len(arr)):
    if k - arr[i] in arr:
        cnt += 1
print(cnt//2)