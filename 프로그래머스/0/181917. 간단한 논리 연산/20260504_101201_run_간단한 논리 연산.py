def solution(x1, x2, x3, x4):
    answer = True
    if x1 or x2 or x3 or x4 == False:
        answer = False
    return answer

# (x1 ∨ x2) ∧ (x3 ∨ x4)
# x	y	x ∨ y	x ∧ y
# T	T	T	    T
# T	F	T	    F
# F	T	T	    F
# F	F	F       F