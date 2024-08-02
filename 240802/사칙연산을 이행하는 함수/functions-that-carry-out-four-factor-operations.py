arr = list(input().split())
result = 0
x, y = int(arr[0]), int(arr[2])
if arr[1] == '+':
    result = x + y
elif arr[1] == '-':
    result = x - y
elif arr[1] == '*':
    result = x * y
else:
    result = int(x / y)

print(f'{x} {arr[1]} {y} = {result}')