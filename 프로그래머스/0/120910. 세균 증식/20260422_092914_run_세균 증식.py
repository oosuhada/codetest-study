def solution(n, t):
    answer = 0
    
    for x in range(0,t+1):
        answer *= n * 2
    
    return answer