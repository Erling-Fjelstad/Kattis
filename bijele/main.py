pieces_list = list(map(int, input().split()))
correct_pieces = [1, 1, 2, 2, 2, 8]

for i in range(len(pieces_list)):
    print(correct_pieces[i] - pieces_list[i], end=" ")