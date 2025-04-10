p = int(input())

def find_index(p, q):
    path = []

    while not (p == 1 and q == 1):
        if p < q:
            path.append("L")
            q -= p
        else:
            path.append("R")
            p -= q

    n = 1
    for step in reversed(path):
        if step == "L":
            n = n * 2
        else:
            n = n * 2 + 1

    return n

for _ in range(p):
    k, frac = input().split()
    num, den = map(int, frac.split("/"))
    idx = find_index(num, den)
    print(f"{k} {idx}")