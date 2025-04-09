from itertools import combinations

boxes = list(map(int, input().split()))
first_tower = boxes.pop(-2)
second_tower = boxes.pop(-1)

first_tower_list = []
second_tower_list = []

for combo in combinations(boxes, 3):
    if sum(combo) == first_tower:
        remaining = [x for x in boxes if x not in combo]
        if sum(remaining) == second_tower:
            first_tower_list = sorted(combo, reverse=True)
            second_tower_list = sorted(remaining, reverse=True)
            break

print(*first_tower_list, *second_tower_list)