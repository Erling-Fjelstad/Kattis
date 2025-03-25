n = int(input())

pizzas = []
prices = []

for i in range(n):
    name, price = input().split()
    pizzas.append(str(name))
    prices.append(int(price))

prices.sort()

sum = 0

if len(prices) % 2 != 0:
    sum += prices[0]
    prices.pop(0)

for i in range(len(prices)):
    if i % 2 != 0:
        sum += prices[i]

print(sum)
        