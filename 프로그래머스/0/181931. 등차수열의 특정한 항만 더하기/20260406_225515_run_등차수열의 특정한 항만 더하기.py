def solution(a, d, included):
    
    n = len(included)
    # a, a+d, a+2d, ... , a+(n-1)*d 
    #included(i)가 true일때만 더함
    
    answer = 0
    
    for i in range(len(included))
        if included(i) == True:
            answer += (a+(i*d))
            
    return answer