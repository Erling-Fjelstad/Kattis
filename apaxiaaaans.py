name = input()

compact_name = name[0]

for i in range(1, len(name)):
    if (name[i] != name[i-1]):
        compact_name += name[i]

print(compact_name)
