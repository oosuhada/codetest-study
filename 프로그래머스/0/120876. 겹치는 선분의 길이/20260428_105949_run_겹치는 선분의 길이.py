def solution(lines):
    [[a1, b1], [a2, b2], [a3, b3]] = lines
    start = min(a1,a2,a3,b1,b2,b3)
    end = max(a1,a2,a3,b1,b2,b3)
    array = list.range(min,max+1)
    answer = 0
    return array