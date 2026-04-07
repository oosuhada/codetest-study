def solution(numLog):
    
    for i in range(len(numLog)):
    c = numLog(i)
    
    if c == 1:
        c = "w"
    elif c == -1:
        c = "s"
    elif c == 10:
        c = "d"
    elif c == -10:
        c = "a"
    
    return numLog
    