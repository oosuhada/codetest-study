def solution(chicken):
    order = (chicken // 10) + (chicken // 100) + (chicken //
1000) + (chicken // 10000) 
    return order