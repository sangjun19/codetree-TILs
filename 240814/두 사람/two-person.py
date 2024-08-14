age1, gen1 = input().split()
age2, gen2 = input().split()
age1 = int(age1)
age2 = int(age2)

if age1 + age2 > 36 and (gen1 == 'M' or gen2 == 'M'):
    print(1)