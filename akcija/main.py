n = int(input())
books = []

for _ in range(n):
    books.append(int(input()))


sorted_books = sorted(books)

count = 0
price = 0
for book in reversed(sorted_books):
    count += 1
    if count % 3 == 0:
        continue
    price += book

print(price)