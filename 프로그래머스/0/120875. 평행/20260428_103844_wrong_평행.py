def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    if (x1-x2) == (x3-x4) and (y1-y2) == (y3-y4):
        return 1
    elif (x1-x3) == (x2-x4) and (y1-y3) == (y2-y4):
        return 1
    elif (x1-x4) == (x2-x3) and (y1-y4) == (y2-y3):
        return 1
    elif (x2-x4) == (x1-x3) and (y2-y4) == (y1-y3):
        return 1
    else:
        return 0

# #평행인지 검증하는 코드 어떻게 구성할 것인가
# ValueError: not enough values to unpack (expected 4, got 2)
# for [a,b],[c,d],[e,f],[g,h] in dots: