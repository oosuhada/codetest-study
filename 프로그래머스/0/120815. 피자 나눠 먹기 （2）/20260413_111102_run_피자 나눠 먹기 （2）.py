def solution(n):
    answer = 0
    i = 1
    #6과 result값의 공배수가 n으로 나눠서 0이 될때 멈춤
    for i>0:
        if i % n == 0 and i % 6 == 0:
            answer += (i % 6)
            return answer
        else:
            i += 1
    
    
  