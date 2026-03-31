def solution(A, B):
    answer = 0
    return A[-3] + A[-2] + A[:-3]

# hello 
# -> ohell : A[-1] + A[:-1]
# -> lohel : A[-2] + A[-1] + A[:-2]
# -> llohe : A[-3] + A[-2] + A[:-3]