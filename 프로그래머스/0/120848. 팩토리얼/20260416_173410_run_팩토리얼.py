def solution(n):
    answer = 1
    c = 1
    
    while answer <= n:
        answer *= c
        c += 1
    
    return answer