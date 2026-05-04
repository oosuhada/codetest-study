def solution(a, b, c, d):
    list_1 = [a, b, c, d]
    list_1.sort()
    x1, x2, x3, x4 = list_1
    
    if x1 == x2 == x3 == x4:
        return 1111 * x1
    elif x1 == x2 == x3:
        return (10 * x1 + x4) * (10 * x1 + x4)
    elif x2 == x3 == x4:
        return (10 * x4 + x1) * (10 * x4 + x1)
    elif (x1 == x2) and (x3 == x4) and (x2 != x3):
        return (x1 + x3) * abs(x1 - x3)
    elif (x1 == x2):
        return x3 * x4
    elif (x2 == x3):
        return x1 * x4
    elif (x3 == x4):
        return x1 * x2
    elif x1 != x2 != x3 != x4:
        return min(list_1) 
    
    

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