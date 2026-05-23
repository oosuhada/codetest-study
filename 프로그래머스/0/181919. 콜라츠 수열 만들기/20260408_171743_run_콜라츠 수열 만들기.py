def solution(n):
    
    result = [x]
    x = n
    
    while x>1:
        if x % 2 == 0:
            x = x/2
            result.append(x)
        else:
            x = (3 * x) + 1
            result.append(x)
    
    return result
