def solution(chicken):
    order = (chicken // 10 + chicken % 10) // 100
    return order


# 입력값 〉	1081
# 기댓값 〉	120
# 실행 결과 〉	실행한 결괏값 119이 기댓값 120과 다릅니다.
# def solution(chicken):
#     order = (chicken // 10) + (chicken // 100) + (chicken //
# 1000) + (chicken // 10000) ...