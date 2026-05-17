def solution(polynomial):
    element = polynomial.split(" + ")
    a = []
    b = []
    
    for c in element:
        if c.has('x'):
            a.append(c)
        else:
            b.append(c)
            
    answer = ''
    return [a,b]