def solution(n, t):
    answer = n
    
    for x in range(0,t):
        answer *= 2
    
    return answer

# def solution(n, t):
#     answer = 0
#     for x in range(0,t+1):
#         answer *= n * 2
#     return answer

# def solution(n, t):
#     answer = 1 
#     for x in range(0,t+1):
#         answer *= n * 2  
#     return answer

# def solution(n, t):
#     answer = n
#     for x in range(0,t+1):
#         answer *= 2
#     return answer