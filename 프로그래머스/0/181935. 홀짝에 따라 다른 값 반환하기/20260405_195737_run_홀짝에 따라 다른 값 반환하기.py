def solution(n):
    
    answer = 0
    
    # 1부터 n까지 반복
    for i in range(1, n+1):
        
    if n % 2 == 1:
        if i % 2 == 1:
            answer += i
    else 
        if i % 2 == 0:
        answer += i*i
        
    return answer