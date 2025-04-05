numbers = sorted(list(map(int, input().split())))
numbers_dict = dict(zip("ABC", numbers))

order = input()
for c in order:
    print(numbers_dict[c], end=" ")
