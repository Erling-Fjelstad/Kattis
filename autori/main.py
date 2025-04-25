name_list = input().split("-")
short_variation = ""

for name in name_list:
    short_variation += name[0]

print(short_variation)