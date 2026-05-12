def solution(n):
    answer = []
    
    for i in n:
        if i < n and (i+1) % 2 == 0:
            answer += i
    
    return answer