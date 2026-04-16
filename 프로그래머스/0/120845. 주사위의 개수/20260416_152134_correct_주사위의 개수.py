def solution(box, n):
    a = box[0]
    b = box[1]
    c = box[2]
    answer = (a//n) * (b//n) * (c//n)
    return answer