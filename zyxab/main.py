n = int(input())

validNames = []
bestName = "a" * 20
for _ in range(n):
    name = input()
    setName = {c for c in name}
    if len(name) < 5:
        continue
    if len(name) != len(setName):
        continue
    if len(name) < len(bestName) or (len(name) == len(bestName) and name > bestName):
        bestName = name

if bestName == "a" * 20:
    print("Neibb")
else:
    print(bestName)
