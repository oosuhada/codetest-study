def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    if (x1-x2) / (y1-y2) == (y3-y4) / (x3-x4):
        return 1
    elif (x1-x3) / (y1-y3) == (y2-y4) / (x2-x4):
        return 1    
    elif (x1-x4) / (y1-y4) == (y2-y3) / (x2-x3):
        return 1  
    elif (x2-x4) / (y2-y4) == (y1-y3) / (x1-x3):
        return 1  
    else:
        return 0

# #평행인지 검증하는 코드 어떻게 구성할 것인가
# ValueError: not enough values to unpack (expected 4, got 2)
# for [a,b],[c,d],[e,f],[g,h] in dots:

# 테스트 1 〉	실패 (0.00ms, 9.28MB)
# 테스트 2 〉	통과 (0.00ms, 9.25MB)
# 테스트 3 〉	통과 (0.00ms, 9.27MB)
# 테스트 4 〉	통과 (0.00ms, 9.23MB)
# 테스트 5 〉	실패 (0.00ms, 9.19MB)
# 테스트 6 〉	통과 (0.00ms, 9.1MB)
# 테스트 7 〉	통과 (0.00ms, 9.35MB)
# 테스트 8 〉	통과 (0.00ms, 9.36MB)
# 테스트 9 〉	통과 (0.00ms, 9.36MB)
# 테스트 10 〉	실패 (0.00ms, 9.1MB)
# 테스트 11 〉	통과 (0.00ms, 9.25MB)
# 테스트 12 〉	통과 (0.00ms, 9.23MB)
# 테스트 13 〉	통과 (0.00ms, 9.23MB)
# 테스트 14 〉	통과 (0.00ms, 9.25MB)
# 테스트 15 〉	통과 (0.00ms, 9.17MB)
# 테스트 16 〉	통과 (0.00ms, 9.25MB)
# 테스트 17 〉	통과 (0.00ms, 9.36MB)
# def solution(dots):
#     [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
#     if (x1-x2) == (x3-x4) and (y1-y2) == (y3-y4):
#         return 1
#     elif (x1-x3) == (x2-x4) and (y1-y3) == (y2-y4):
#         return 1
#     elif (x1-x4) == (x2-x3) and (y1-y4) == (y2-y3):
#         return 1
#     elif (x2-x4) == (x1-x3) and (y2-y4) == (y1-y3):
#         return 1
#     else:
#         return 0
# 현재 작성하신 코드는 두 선분의 $\Delta x$와 $\Delta y$가 완전히 같을 때(길이와 방향이 같을 때)만 1을 리턴하고 있습니다. 하지만 평행은 '기울기'가 같으면 성립하며, 기울기는 비율의 문제입니다.