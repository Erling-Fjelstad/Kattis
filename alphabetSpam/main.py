text = input()

total = len(text)

whitespace = 0
lowercase = 0
uppercase = 0
symbol = 0

for c in text:
    if c == '_':
        whitespace += 1
    elif 97 <= ord(c) <= 122:
        lowercase += 1
    elif 65 <= ord(c) <= 90:
        uppercase += 1
    else:
        symbol += 1

print(whitespace/total)
print(lowercase/total)
print(uppercase/total)
print(symbol/total)