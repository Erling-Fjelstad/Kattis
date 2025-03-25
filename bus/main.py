cases = int(input())

for i in range(cases):
    busstops = int(input())

    n = 0
    
    for i in range(busstops):
        n = n * 2 + 1 

    print(n)
