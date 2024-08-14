age1, gen1 = input().split()
age2, gen2 = input().split()
age1 = int(age1)
age2 = int(age2)

if (age1 > 18 and gen1 == 'M') or (age2 > 1 and gen2 == 'M'):
    print(1)