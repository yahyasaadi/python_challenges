# def solution(A):
#     count = 0
#     for i in range(len(A)):
        
#         for j in range(len(A)):
#             if A[i] == A[j]:
#                 count += 1

#         if count % 2 != 0:
#             return A[i]
#     return -1
def solution(A):
   result = 0
   for number in A:
     result ^= number
   return result

# print(solution([9, 3, 9, 3, 9, 7, 9]))
print(sorted([9, 3, 9, 3, 9, 7, 9]))