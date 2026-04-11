def solution(A, B):
    n = len(A)
    for i in range(n):
        if A[-i:] + A[:-i] == B:
            return i
    return -1

# def solution(A, B):
#     n = len(A)
#     for i in range(n):
#         if A[-i:] + A[:-i] == B:
#             return i
#         else:
#             return -1
# 이건 틀렸고

# def solution(A, B):
#     n = len(A)
#     for i in range(n):
#         if A[-i:] + A[:-i] == B:
#             return i
#     return -1
# 이건 맞은 이유가 뭘까?


# hello 
# -> ohell : A[-1] + A[:-1]
# -> lohel : A[-2] + A[-1] + A[:-2]
# -> llohe : A[-3] + A[-2] + A[-1] + A[:-3]

# hello 
# -> ohell : A[-1] + A[:-1]
# -> lohel : A[-2:] + A[:-2]
# -> llohe : A[-3:] + A[:-3]