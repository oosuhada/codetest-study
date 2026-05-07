def solution(n):
    x = list(range(3*n))
    xx = []

    for i in x:
        if i % 3 != 0 and '3' not in str(i):
            xx.append(i)
    
    return xx

# 3x 마을에서 쓰는 숫자 x까지의 정수 배열 - 3의 배수 개수 - 3이 포함된 숫자 개수 + (3의 배수이면서 3이 포함된 숫자 개수) = 10진법 숫자 n

# 3x 마을에서 쓰는 숫자 x = 10진법 숫자 n + 3의 배수 개수 + 3이 포함된 숫자 개수 -  (3의 배수이면서 3이 포함된 숫자 개수)

#     for k in range(n):
#         if str(k).contains('3'):
# AttributeError: 'str' object has no attribute 'contains'
# AttributeError: 'str' object has no attribute 'contain'
# AttributeError: 'str' object has no attribute 'has'

# x를 모르는 상태에서 n까지의 배열을 가지고 계산을 하기 때문에 수식이 맞지 않음.
# def solution(n):
#     x = n
#     answer = n
#     for i in range(n):
#         if i % 3 == 0:
#             answer += 1
#     for k in range(n):
#         if '3' in str(k):
#             answer += 1
#     return answer

# def solution(n):
#     x = 3*n
#     xx = range(3*n)
#     for i in range(x):
#         if i % 3 == 0:
#             xx.delete(i)
#     for k in range(x):
#         if '3' in str(k):
#             xx.delete(k) 
#     return xx

# xx = range[0:x]으로 시도하다가 안되서 문법 검색함
# 0부터 n-1까지: list(range(n)) 

# AttributeError: 'list' object has no attribute 'delete'
#     for i in range(x):
#         if i % 3 == 0:
#             xx.delete(i)
#     for k in range(x):
#         if '3' in str(k):
#             xx.delete(k)