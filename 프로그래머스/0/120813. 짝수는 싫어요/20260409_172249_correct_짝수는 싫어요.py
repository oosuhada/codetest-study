def solution(n):
    answer = []
    
    for i in range(0,n+2):
        if i <= n and (i+1) % 2 == 0:
            answer.append(i)
    
    return answer