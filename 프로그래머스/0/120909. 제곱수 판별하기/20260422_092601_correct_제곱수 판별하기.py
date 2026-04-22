def solution(n):
    answer_x = 0
    for x in range(0,1001):
        if (x*x) == n:
            answer_x += 1
        else:
            answer_x += 0
            
    if answer_x == 1:
        return 1
    else:
        return 2

        
# 입력값 〉	144
# 실행 결과 〉	실행한 결괏값 2이 기댓값 1과 다릅니다. 

# def solution(n):
#     for x in range(1,1001):
#         if x * x == n:
#             return 1
#         else:
#             return 2

# def solution(n):
#     for x in range(0,1001):
#         if (x * x) == n:
#             return 1
#             break;
#         else:
#             return 2