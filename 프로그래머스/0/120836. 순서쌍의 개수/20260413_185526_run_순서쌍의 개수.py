def solution(n):
    answer = 0
    i = 1
    
    while i>0 and i<n:
        if n % i == 0:
            answer += 1
            i += 1
        else:
            i += 1
    
    return answer