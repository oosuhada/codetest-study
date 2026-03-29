def solution(numer1, denom1, numer2, denom2):

    #answer_double = (numer1 / denom1) + (numer2 / denom2)
    #기약 분수로 나타내는 방법 어떻게?
    
    [a,b] = [,]
    result = [a,b]
    
    
    #셋다 for로 할지 if - elif로 묶을지 고민
    if denom1 > denom2:
        if denom1 % denom1 == 0:
            a += numer1 + (numer2 * (denom1/denom2))
            b += denom1
        else:
            a += (numer1 * denom2) + (numer2 * denom1)
            b += denom1 * denom2
            
    elif denom1 < denom2:
        if denom2 % denom1 == 0:
            a += (numer1 * (denom2/denom1)) + numer2
            b += denom2
        else:
            a += (numer1 * denom2) + (numer2 * denom1)
            b += denom1 * denom2
        
    elif denom1 == denom2:
        a += numer1 + numer2
        b += denom1
        
    return result