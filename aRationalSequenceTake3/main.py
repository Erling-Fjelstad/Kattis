p = int(input())

def F(n):
    p, q = 1, 1  
    path = []

    while n > 1:
        if n % 2 == 0:
            path.append("L")
        else:
            path.append("R")
        n //= 2

    for direction in reversed(path):
        if direction == "L":
            q = p + q
        else:
            p = p + q

    return f"{p}/{q}"

            

for _ in range(p):
    p, n = map(int, input().split())
    print(p, F(n))