def solution(dots):
    for [a,b],[c,d],[e,f],[g,h] in dots:
        if (c - a) == (g - e) and (d - b) == (h - f):
            return 1
        else:
            return 0

#평행인지 검증하는 코드 어떻게 구성할 것인가
