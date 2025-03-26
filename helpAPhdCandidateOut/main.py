test_cases = int(input())

for i in range(test_cases):
    line = input()
    if "=" in line:
        print("skipped")
        continue
    
    a, b = list(map(int, line.split("+")))
    print(a + b)