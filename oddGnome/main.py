groups = int(input())

for i in range(groups):
    gnomes = list(map(int, input().split()))
    numberOfGnomes = gnomes.pop(0)
    
    for j in range(numberOfGnomes - 1):
        if (gnomes[j + 1] - gnomes[j]) != 1:
            print(j + 2)
            break