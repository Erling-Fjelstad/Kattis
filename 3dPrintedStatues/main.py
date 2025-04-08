import math

statues = int(input())
minimum = statues 

for i in range(2, (statues + 1) // 2 + 1):
    days_to_build_printers = math.log2(i)
    days = days_to_build_printers + statues / i
    minimum = min(minimum, int(math.ceil(days)))

print(minimum)


