import math

string_of_char = input()

sum_char = 0

for c in string_of_char:
    sum_char += ord(c)  

avarage = math.floor(sum_char/len(string_of_char))

avarage_char = chr(avarage) 

print(avarage_char)
