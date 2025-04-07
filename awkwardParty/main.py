n = int(input())

guests = list(map(int, input().split()))
minimum = n

guests_dict = {}

for i, guest in enumerate(guests):
    if guest in guests_dict:
        dist = i - guests_dict[guest]
        minimum = min(dist, minimum)
    guests_dict[guest] = i

print(minimum)
