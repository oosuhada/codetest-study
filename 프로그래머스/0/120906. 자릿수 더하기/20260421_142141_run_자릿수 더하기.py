def solution(n):
    str_n = str(n)
    answer = 0
    
    for c in str_n:
        answer += c
        
    return answer