# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # maximum = []
    # for i in range(len(A)):
    #     if (A[i] % 3) == 0:
    #         maximum.append(A[i])
    # return max(maximum)
    return max([A[i] for i in range(len(A)) if A[i] % 3 == 0])


print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
print(solution([3, 6, 9, 12, 15, 18, 21, 24, 27, 30]))


# def solution(A, B, X, Y):
#     # write your code in Python 3.6
#     radius_range = 20

#     upper_bound_a = [x + 20 for x in A]
#     lower_bound_a = [x - 20 for x in A]
#     upper_bound_b = [x + 20 for x in B]
#     lower_bound_b = [x - 20 for x in B]

#     for i in range(len(A)):
#         if A[i] == X and B[i] == Y:
#             return i
#         elif (A[i] + 20) == (X + 20) and B[i] == Y:
#             return i
#     return 0


# print(solution([100, 200, 100], [50, 100, 100], 100, 100))
# print(solution([100, 200, 100], [100, 100, 50], 120, 100))