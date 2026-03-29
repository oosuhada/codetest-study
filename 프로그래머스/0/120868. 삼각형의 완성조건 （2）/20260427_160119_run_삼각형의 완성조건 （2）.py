def solution(sides):
    a = max(sides)
    b = min(sides)
    answer = 0
    
    #1 ≤ sides의 원소 ≤ 1,000
    #1 ≤ c ≤ 2,001
    
    for c in range(2001):
        if c > a and a + b > c:
            answer += 1
        elif c < a and a < b + c:
            answer += 1
        elif c == a:
            answer += 1
    return answer
    
    
    