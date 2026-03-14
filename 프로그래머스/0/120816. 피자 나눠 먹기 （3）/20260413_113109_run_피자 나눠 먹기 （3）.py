def solution(slice, n):
    answer = 0
    x = 1
    while x >= 1:
        if slice * x >= n:
            answer += x
    
    return answer