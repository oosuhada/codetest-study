def solution(slice, n):
    answer = 0
    x = 1
    
    while x >= 1:
        if slice * x >= n:
            answer += min(x)
            break;
    
    return answer

#실행 시간이 10.0초를 초과하여 실행이 중단되었습니다.