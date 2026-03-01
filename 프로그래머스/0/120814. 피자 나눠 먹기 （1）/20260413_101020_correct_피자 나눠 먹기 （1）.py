import math
def solution(n):
    
    answer = 0
    
    x = n//7
    if n % 7 == 0:
        answer += x
    else:
        answer += x+1
        #answer += math.ceil(x)+1
    #ceil 함수 검색해봄. n//7 의 결과값 정수인지 확인 필요
    
    return answer