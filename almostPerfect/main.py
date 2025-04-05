def perfectNumber(p):
    count = 1  
    i = 2
    while i * i <= p:
        if p % i == 0:
            count += i
            if i != p // i and p // i != p:
                count += p // i
        i += 1
    
    if count == p:
        print(p, "perfect")
    elif abs(p - count) <= 2:
        print(p, "almost perfect")
    else:
        print(p, "not perfect")

try:
    while True:
        p = int(input())
        perfectNumber(p)
except:
    pass