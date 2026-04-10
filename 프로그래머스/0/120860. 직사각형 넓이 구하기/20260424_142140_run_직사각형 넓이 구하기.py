def solution(dots):
    a, b, c, d = dots
    x1, y1 = a
    return x1

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