n = int(input())
arr = list(input())
stack = []
num = []
for i in range(n):
    num.append(int(input()))

stack.append(num[ord(arr.pop(0)) - ord('A')])
while arr:
    temp = arr.pop(0)
    if temp.isalpha():
        stack.append(num[ord(temp) - ord('A')])
    else:
        y, x = stack.pop(), stack.pop()                
        if temp == '+':
            stack.append(x + y)
        elif temp == '-':
            stack.append(x - y)
        elif temp == '*':
            stack.append(x * y)
        elif temp == '/':
            stack.append(x / y)
    # print(stack)
print(f"{stack[0]:.2f}")