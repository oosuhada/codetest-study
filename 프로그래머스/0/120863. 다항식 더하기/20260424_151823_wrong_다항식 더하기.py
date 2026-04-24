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
    
    for y in b:
        e += int(y)
    
    if e == 0 and d == 0:
        answer = str(0)
    elif d == 0 and e != 0:
        answer = str(e)
    elif e == 0 and d != 1:
        answer = str(d)+'x'
    elif e == 0 and d == 1:
        answer = 'x'
    elif d == 1:
        answer = 'x + '+str(e)
    else:
        answer = str(d)+'x + '+str(e)
    
    return answer

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

# 테스트 1 〉	통과 (0.02ms, 9.31MB)
# 테스트 2 〉	통과 (0.02ms, 9.35MB)
# 테스트 3 〉	통과 (0.01ms, 9.23MB)
# 테스트 4 〉	통과 (0.02ms, 9.22MB)
# 테스트 5 〉	통과 (0.02ms, 9.37MB)
# 테스트 6 〉	통과 (0.03ms, 9.3MB)
# 테스트 7 〉	통과 (0.02ms, 9.29MB)
# 테스트 8 〉	실패 (0.03ms, 9.33MB)
# 테스트 9 〉	통과 (0.02ms, 9.27MB)
# 테스트 10 〉	실패 (0.00ms, 9.1MB)
# 테스트 11 〉	통과 (0.02ms, 9.23MB)
# 테스트 12 〉	실패 (0.03ms, 9.31MB)
# def solution(polynomial):
#     element = polynomial.split(" + ")
#     a = []
#     b = []
    
#     for c in element:
#         if 'x' in c:
#             a.append(c)
#         else:
#             b.append(c)
    
#     d = 0
#     e = 0
#     for x in a:
#         if x == 'x':
#             d += 1
#         else:
#             d += int(x.replace('x',''))
    
#     for y in b:
#         e += int(y)
    
#     if e == 0 and d == 0:
#         answer = str(0)
#     elif d == 0:
#         answer = str(e)
#     elif e == 0:
#         answer = str(d)+'x'
#     else:
#         answer = str(d)+'x + '+str(e)
    
#     return answer

# 테스트 1 〉	통과 (0.02ms, 9.18MB)
# 테스트 2 〉	통과 (0.02ms, 9.33MB)
# 테스트 3 〉	통과 (0.01ms, 9.12MB)
# 테스트 4 〉	통과 (0.02ms, 9.33MB)
# 테스트 5 〉	통과 (0.02ms, 9.34MB)
# 테스트 6 〉	통과 (0.02ms, 9.34MB)
# 테스트 7 〉	통과 (0.02ms, 9.22MB)
# 테스트 8 〉	실패 (0.02ms, 9.22MB)
# 테스트 9 〉	통과 (0.03ms, 9.29MB)
# 테스트 10 〉	실패 (0.00ms, 9.2MB)
# def solution(polynomial):
#     element = polynomial.split(" + ")
#     a = []
#     b = []
    
#     for c in element:
#         if 'x' in c:
#             a.append(c)
#         else:
#             b.append(c)
    
#     d = 0
#     e = 0
#     for x in a:
#         if x == 'x':
#             d += 1
#         else:
#             d += int(x.replace('x',''))
    
#     for y in b:
#         e += int(y)
    
#     if e == 0 and d == 0:
#         answer = str(0)
#     elif d == 0 and e != 0:
#         answer = str(e)
#     elif e == 0 and d != 0:
#         answer = str(d)+'x'
#     else:
#         answer = str(d)+'x + '+str(e)
    
#     return answer

# "d == 1일 때 따로 처리해야 함" 이라고 gpt한테 물어봄