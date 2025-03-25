n = int(input())
rocks = list(map(int, input().split()))

index_map = {rock: i for i, rock in enumerate(sorted(rocks))}

for rock in rocks:
    print(index_map[rock], end=" ")