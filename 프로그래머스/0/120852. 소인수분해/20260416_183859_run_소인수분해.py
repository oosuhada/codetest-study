def solution(n):

    answer1 = []
    for c in range(2,n+1):
        if n % c == 0:
            for i in range(1,c-1):
                if c % i != 0:
                    answer1.append(c)
    return answer1


        
        
#TypeError: 'int' object is not iterable
# def solution(n):

#     answer = []
#     for c in range(2,n):
#         if n % c == 0:
#             answer += c
#     return answer

# answer += c와 answer.append(c)의 차이 다시 학습하기
# answer.append(c)로 풀이했을때 입력값 12의 기댓값 [2, 3], 실행값 [2,3,4,6]
# 소수만 나올때까지 반복하는 방법 필요함 -> 소수 구하는 방법 구글링


