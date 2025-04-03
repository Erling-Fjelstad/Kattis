grid = []

for _ in range(4):
    row = list(map(int, input().split()))
    grid.append(row)

operation = int(input())

def correct_list(rowOrCol, reversed):
    new_list = [x for x in rowOrCol if x != 0]
    if reversed:
        for i in range(len(new_list) - 1, 0, -1):
            if new_list[i] == new_list[i - 1]:
                new_list[i] *= 2
                new_list.pop(i - 1)
                new_list.insert(0, 0)
        while len(new_list) < 4:
            new_list.insert(0, 0)
    else:
        for i in range(len(new_list) - 1):
            if new_list[i] == new_list[i + 1]:
                new_list[i + 1] *= 2
                new_list.pop(i)
                new_list.append(0)
        while len(new_list) < 4:
            new_list.append(0)       
    return new_list

if operation == 0:
    for i in range(len(grid)):
        grid[i] = correct_list(grid[i], False)
elif operation == 1:
    for i in range(len(grid)):
        col = []
        for j in range(len(grid[i])):
            col.append(grid[j][i])
        col = correct_list(col, False)
        for h in range(len(col)):
            grid[h][i] = col[h]
elif operation == 2:
    for i in range(len(grid)):
        grid[i] = correct_list(grid[i], True)
elif operation == 3:
    for i in range(len(grid)):
        col = []
        for j in range(len(grid[i])):
            col.append(grid[j][i])
        col = correct_list(col, True)
        for h in range(len(col)):
            grid[h][i] = col[h]

for list in grid:
    for number in list:
        print(number, end=" ")
    print("\n")
        
