area = int(input())

#Heron's method
x = area
while True:
    x_1 = (x + area / x) / 2
    if abs(x - x_1) < 10 ** (-7):
        x_1 = x
        break
    x = x_1

fence_length = 4 * x_1
print(fence_length)

