def find_i(number_x0):
    if number_x0 == "1":
        return 1
    
    count = 0
    while True:
        if len(number_x0) == 1:
            return count + 2
        number_x0 = str(len(number_x0))
        count += 1

while True:
    s = input()
    
    if s == "END":
        break

    print(find_i(s))

