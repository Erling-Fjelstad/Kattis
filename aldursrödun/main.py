from itertools import permutations

childrens = int(input())
ages = list(map(int, input().split()))

#Eukilds algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for p in permutations(ages):
    p = list(p)
    test = True
    for i in range(len(p) - 1):
        if gcd(p[i], p[i+1]) == 1:
            test = False
    if test:
        for age in p:
            print(age, end = " ")
        quit()

print("Neibb")



