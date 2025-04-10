n = int(input())
n_list = list(map(int, input().split()))
a = 1

for number in n_list:
    a *= number

m = int(input())
m_list = list(map(int, input().split()))
b = 1

for number in m_list:
    b *= number

while b != 0:
    a, b = b, a % b

gcd = str(a)
if len(gcd) > 9:
    print(gcd[-9:])
else:
    print(a)