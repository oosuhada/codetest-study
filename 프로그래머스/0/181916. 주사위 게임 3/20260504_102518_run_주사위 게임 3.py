def solution(a, b, c, d):
    list_1 = [a, b, c, d]
    list_1.sort()
    x1, x2, x3, x4 = list_1
    answer = 0
    return list_1

# AttributeError: 'list' object has no attribute 'sorted'
# def solution(a, b, c, d):
#     list = [a, b, c, d]
#     a1, b1, c1, d1 = list.sorted()
#     return list

# def solution(a, b, c, d):
#     list_1 = [a, b, c, d]
#     a1, b1, c1, d1 = list_1.sorted()
#     answer = 0
#     return list_1

# TypeError: cannot unpack non-iterable NoneType object
# def solution(a, b, c, d):
#     list_1 = [a, b, c, d]
#     a1, b1, c1, d1 = list_1.sort()
#     return list_1

# def solution(a, b, c, d):
#     list_1 = [a, b, c, d]
#     [a1, b1, c1, d1] = list_1.sort()
#     return list_1