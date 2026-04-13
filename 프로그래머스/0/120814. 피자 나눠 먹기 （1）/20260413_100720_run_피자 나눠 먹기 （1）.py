def solution(n):
    
    answer = 0
    
    if n % 7 == 0:
        answer += n//7
    else:
        answer += (n//7).ceil
    #ceil 함수 검색해봄
    
    return answer