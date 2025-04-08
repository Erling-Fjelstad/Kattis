n = int(input())
up = n
down = n

while True:
    if n < 99:
        print(99)
        break
    if up % 100 == 99:
        print(up)
        break
    if down > 0 and down % 100 == 99:
        print(down)
        break
    up += 1
    down -= 1
