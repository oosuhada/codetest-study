def solution(dots):
    a, b, c, d = dots
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d
    
    width = abs(x2 - x1)
    height = abs(y3 - y2)
    
    return width * height

# ValueError: not enough values to unpack (expected 4, got 2)
# def solution(dots):
#     for [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] in dots:
#         answer = [x1, y1]
#     return answer

# def solution(dots):
#     for [a,b,c,d] in dots:
#         answer = a
#     return answer

# python array unpack 방법 검색함
# a, b, c, d = dots

# python definite difference between two minus numbers 검색함
# diff = abs(x - y)

# 테스트 1 〉	실패 (0.00ms, 9.25MB)
# 테스트 2 〉	실패 (0.00ms, 9.01MB)
# 테스트 3 〉	실패 (0.00ms, 9.25MB)
# 테스트 4 〉	실패 (0.00ms, 9.27MB)
# 테스트 5 〉	실패 (0.00ms, 9.2MB)
# def solution(dots):
#     a, b, c, d = dots
#     x1, y1 = a
#     x2, y2 = b
#     x3, y3 = c
#     x4, y4 = d
    
#     width = abs(x2 - x1)
#     height = abs(y2 - y3)
    
#     return width * height