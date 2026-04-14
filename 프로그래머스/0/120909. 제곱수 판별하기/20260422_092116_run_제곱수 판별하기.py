def solution(n):
    for x in range(1,1001):
        if x * x == n:
            return 1
        else:
            return 2