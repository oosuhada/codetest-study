def solution(polynomial):
    element = polynomial.split(" + ")
    a = []
    b = []
    
    for c in element:
        if 'x' in c:
            a.append(c)
        else:
            b.append(c)
            
    answer = ''
    return [a,b]

# AttributeError: 'str' object has no attribute 'has'
# def solution(polynomial):
#     element = polynomial.split(" + ")
#     a = []
#     b = []
    
#     for c in element:
#         if c.contains('x'):
#             a.append(c)
#         else:
#             b.append(c)
            
#     answer = ''
#     return [a,b]