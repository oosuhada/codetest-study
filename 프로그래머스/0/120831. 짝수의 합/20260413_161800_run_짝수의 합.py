def solution(n):
    answer = 0
    
    #1부터 n까지의 list 배열이 for c in range(n+1)가 아닌것 같음.
    #    for c in list.range(0,n+1): 도 아님
    for c in list(range(0,n+1)):
        if c % 2 == 0:
            answer += c

    return answer

# TypeError: 'type' object is not subscriptable
# def solution(n):
#     answer = 0
    
#     for c in range[:n+1]:
#         if c % 2 == 0:
#             answer += c

#     return answer