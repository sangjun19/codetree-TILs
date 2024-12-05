n, k = map(int, input().split())
people = set(map(int, input().split()))
people = list(people)
people.sort()
total = 0
dif = []
for i in range(len(people) - 1):
    temp = people[i + 1] - people[i]
    total += temp
    dif.append(temp)
dif.sort()
dif.reverse()
for i in range(k - 1):
    total -= dif[i]
    
print(total)