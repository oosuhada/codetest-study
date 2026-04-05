def solution(a, b):
    
    # 1. 문자열로 변환해서 이어 붙이기
    ab = int(str(a) + str(b))  # a ⊕ b
    ba = int(str(b) + str(a))  # b ⊕ a
    
    # 2. 더 큰 값 반환
    if ab >= ba:
        return ab
    else:
        return ba