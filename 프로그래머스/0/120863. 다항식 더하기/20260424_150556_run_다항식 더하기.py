def solution(polynomial):
    element = polynomial.split(" + ")
    a = []
    b = []
    
    for c in element:
        if 'x' in c:
            a.append(c)
        else:
            b.append(c)
    
    d = 0
    e = 0
    for x in a:
        if x == 'x':
            d += 1
        else:
            d += int(x.replace('x',''))
        
    answer = ''
    return [d,e]

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

# AttributeError: 'str' object has no attribute 'remove'
#    d = 0
#     e = 0
#     for x in a:
#         if x == 'x':
#             d += 1
#         else:
#             d += int(x.remove('x'))
        
#     answer = ''
#     return [d,e]