x, y = map(int, input().split())

r = int(input())

upper_left_corner_x = x - r
upper_left_corner_y = y + r
print(f'{upper_left_corner_x} {upper_left_corner_y}')

lower_left_corner_x = x - r
lower_left_corner_y = y - r
print(f'{lower_left_corner_x} {lower_left_corner_y}')

lower_right_corner_x = x + r
lower_right_corner_y = y - r
print(f'{lower_right_corner_x} {lower_right_corner_y}')

upper_right_corner_x = x + r
upper_right_corner_y = y + r
print(f'{upper_right_corner_x} {upper_right_corner_y}')