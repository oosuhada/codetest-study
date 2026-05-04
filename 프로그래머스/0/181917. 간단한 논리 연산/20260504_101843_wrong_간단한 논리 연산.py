def solution(x1, x2, x3, x4):
    answer = True
    if (x1 and x2 == False) or (x3 and x4 == False):
        answer = False
    return answer

# (x1 ∨ x2) ∧ (x3 ∨ x4)

# x	y	x ∨ y	x ∧ y
# T	T	  T	      T
# T	F	  T	      F
# F	T	  T	      F
# F	F	  F       F

# 테스트 1 〉	실패 (0.00ms, 9.22MB)
# 테스트 2 〉	통과 (0.00ms, 8.89MB)
# 테스트 3 〉	실패 (0.00ms, 8.99MB)
# 테스트 4 〉	실패 (0.00ms, 9.22MB)
# 테스트 5 〉	통과 (0.00ms, 9.23MB)
# 테스트 6 〉	실패 (0.00ms, 9.14MB)
# 테스트 7 〉	실패 (0.00ms, 9.21MB)
# 테스트 8 〉	실패 (0.00ms, 9.23MB)
# 테스트 9 〉	실패 (0.00ms, 9.24MB)
# 테스트 10 〉	실패 (0.00ms, 9.19MB)
# 테스트 11 〉	통과 (0.00ms, 9.22MB)
# 테스트 12 〉	통과 (0.00ms, 9.3MB)
# 테스트 13 〉	실패 (0.00ms, 9.18MB)
# 테스트 14 〉	실패 (0.00ms, 9.08MB)
# 테스트 15 〉	통과 (0.00ms, 9.23MB)
# 테스트 16 〉	통과 (0.00ms, 9.21MB)
# def solution(x1, x2, x3, x4):
#     answer = True
#     if x1 and x2 == False or x3 and x4 == False:
#         answer = False
#     return answer