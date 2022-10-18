"""
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""
"""
matrix -->
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
"""



def diagonalDifference(arr):
    # Write your code here
    left_to_right = sum([arr[i][i] for i in range(len(arr))])
    right_to_left = sum([arr[i][len(arr)-i-1] for i in range(len(arr))])
    return abs(left_to_right-right_to_left)


print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))
print(diagonalDifference([[1,2,3],[4,5,6],[7,8,9]]))
print(diagonalDifference([[1,2,3,4],[5,6,7,8],[8,7,6,5],[4,3,2,1]]))
    


# size = int(input("Input the size of the matrix: "))
# matrix = [[0] * size for row in range(0, size)]
# for x in range(0, size):

#     line = list(map(int, input().split()))

#     for y in range(0, size):
#         matrix[x][y] = line[y]
        
        
# matrix_sum_left_to_right = sum([matrix[i][i] for i in range(size)])
# matrix_sum_right_to_left = sum([matrix[i][size - i - 1] for i in range(size)])

# print(matrix_sum_left_to_right)
# print(matrix_sum_right_to_left)
    