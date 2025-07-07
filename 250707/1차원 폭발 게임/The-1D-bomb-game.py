n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.

flag = False

while True:
    cnt = 1
    flag = True
    for i in range(0, len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            cnt += 1

        if cnt >= m and (numbers[i] != numbers[i + 1]):
            del numbers[i - cnt + 1 : i + 1]
            # print(numbers)
            cnt = 1
            flag = False
            break

    if cnt >= m:
        del numbers[len(numbers) - cnt : len(numbers)]
        flag = False

    if flag: break

print(len(numbers))
for n in numbers:
    print(n)