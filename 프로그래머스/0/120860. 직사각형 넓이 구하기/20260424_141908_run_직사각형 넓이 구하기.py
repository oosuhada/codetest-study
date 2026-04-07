def solution(dots):
    for [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] in dots:
        answer = x1
    return answer

# ValueError: not enough values to unpack (expected 4, got 2)
# def solution(dots):
#     for [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] in dots:
#         answer = [x1, y1]
#     return answer