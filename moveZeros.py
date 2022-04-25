
def move_zeros(array):
    no_zero = [i for i in array if i!=0]
    with_zero = [y for y in array if y==0]
    return no_zero+with_zero

print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
# print(move_zeros([9, 0, 9, 0, 1, 2, 1, 0, 1, 3]))
# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
# print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))