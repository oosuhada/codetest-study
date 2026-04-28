def solution(n):
    x = n
    answer = n
    
    for i in range(n):
        if i % 3 == 0:
            answer += 1
    for k in range(n):
        if str(k).contain('3'):
            answer += 1
    
    return answer


# 3x 마을에서 쓰는 숫자 x까지의 정수 배열 - 3의 배수 개수 - 3이 포함된 숫자 개수 + (3의 배수이면서 3이 포함된 숫자 개수) = 10진법 숫자 n

# 3x 마을에서 쓰는 숫자 x = 10진법 숫자 n + 3의 배수 개수 + 3이 포함된 숫자 개수 -  (3의 배수이면서 3이 포함된 숫자 개수)

#     for k in range(n):
#         if str(k).contains('3'):
# AttributeError: 'str' object has no attribute 'contains'
