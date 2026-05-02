def solution(n):
    answer = 1
    c = 1
    
    while answer <= n:
        answer *= c
        c += 1
    
    return c-2

#팩토리얼 while 문은 만들었는데 결과값이 왜 c가 아니고 c-2가 되어야 하는지는 아직 이해하지 못했음