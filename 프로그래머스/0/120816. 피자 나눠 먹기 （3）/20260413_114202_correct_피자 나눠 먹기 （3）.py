def solution(slice, n):
    answer = 0
    x = 1
    
    while x >= 1:
        if slice * x >= n:
            return x
        else:
            x += 1
    

#실행 시간이 10.0초를 초과하여 실행이 중단되었습니다.

# import math

# def solution(slice, n):
#     return math.ceil(n / slice)

# def solution(slice, n):
#     return ((n - 1) // slice) + 1

# ceil(n / slice)  ==  (n - 1) // slice + 1
