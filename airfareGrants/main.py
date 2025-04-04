flights = int(input())

minimum = 10**5
maximum = 0

for _ in range(flights):
    flight = int(input())
    if flight < minimum:
        minimum = flight
    if flight > maximum:
        maximum = flight

sponsors = int(maximum / 2)

price = minimum - sponsors

if price < 0:
    print(0)
else:
    print(price)