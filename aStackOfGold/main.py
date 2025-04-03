w, s = map(int, input().split())

c = int(s * (s + 1) / 2)

w -= (c * 29260)

stack = int(w / 110)

print(stack)


