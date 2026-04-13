def solution(n):
    answer = 0
    
    for c in range(0:n+1):
        if c % 2 == 0:
            answer += c

    return answer