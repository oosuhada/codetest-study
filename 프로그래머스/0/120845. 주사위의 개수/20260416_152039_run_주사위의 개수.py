def solution(box, n):
    for [a,b,c] in box:
    answer = (a//n) * (b//n) * (c//n)
    return answer