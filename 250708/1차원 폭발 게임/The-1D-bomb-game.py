n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.

flag = False

while True:
    i = 0
    flag = True
    while i < len(numbers):
        j = i + 1
        while j < len(numbers) and numbers[j] == numbers[i]:
            j += 1               # [i, j) 가 같은 숫자 구간
        if j - i >= m:           # m개 이상이면
            del numbers[i:j]
            flag = False
            break                # 삭제했으니 처음부터 재검사
        i = j                    # 아니면 다음 구간으로
    if flag:
        break

print(len(numbers))
for n in numbers:
    print(n)