def solution(n):
    answer = []
    
    for c in range(1, n+1):
        if n % c == 0:
            answer.append(c)
            
    return answer


# TypeError: 'type' object is not subscriptable
# def solution(n):
#     answer = []
#     for c in range[0:n+1]:
#         if n % c == 0:
#             answer.append(c)
#     return answer

# for c in range(1:n+1): 에서 range와 슬라이싱 문법 혼용해서 사용함 구분해서 학습 필요