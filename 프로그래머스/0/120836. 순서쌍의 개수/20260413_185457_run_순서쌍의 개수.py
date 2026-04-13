def solution(n):
    answer = 0
    
    while i>0, i<n:
        if n % i == 0:
            answer += 1
            i += 1
        else:
            i += 1
    
    return answer