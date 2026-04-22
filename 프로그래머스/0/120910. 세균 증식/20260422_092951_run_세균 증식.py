def solution(n, t):
    answer = n
    
    for x in range(0,t+1):
        answer *= 2
    
    return answer