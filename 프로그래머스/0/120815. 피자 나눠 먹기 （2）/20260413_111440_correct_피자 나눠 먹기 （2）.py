def solution(n):
    answer = 0
    i = 1
    #6과 result값의 공배수가 n으로 나눠서 0이 될때 멈춤
    while i>0: #while 대신 for문을 사용하여 틀림. 두 개념 정확히 구분 필요
        if i % n == 0 and i % 6 == 0:
            answer += (i // 6)
            return answer
        else:
            i += 1
    
    #lcm, gcd 개념도 학습해서 사용하면 더 빠른 풀이 가능할듯
    
    
  